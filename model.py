from sqlalchemy import create_engine, Column, Integer, String, Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,backref

engine = create_engine('sqlite:///records.db', echo=False)

Base = declarative_base()

class City(Base):
	__tablename__ = "cities"
	ct_id = Column(Integer, primary_key=True)
	ct_name = Column(String, nullable=False)
	ct_latitude = Column(Float)
	ct_longitude = Column(Float)
	ct_records = relationship("TempRecord")

class TempRecord(Base):
	__tablename__ = "temprecords"
	tmr_id = Column(Integer, primary_key=True)
	tmr_timezone = Column(String)
	tmr_current_time = Column(Integer, unique=True)
	tmr_sunrise = Column(Integer)
	tmr_sunset = Column(Integer)
	tmr_temperature = Column(Float)
	tmr_feels_like = Column(Float)
	tmr_pressure = Column(Float)
	tmr_humidity = Column(Float)
	tmr_weather_main = Column(String)
	tmr_description = Column(String)
	tmr_city = Column(Integer, ForeignKey("cities.ct_id"))

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
sess = session()


def add_city(name, lat, lon):
	city = City(ct_name=name, ct_latitude=lat, ct_longitude=lon)
	sess.add(city)
	sess.commit()
	return True

def view_city():
	cities = sess.query(City)
	return cities

def add_city_records(name, tz, ct, sr,ss,temp, fl, press, hum, wm, desc):
	city = sess.query(City).filter(City.ct_name == name).first()
	city.ct_records = [TempRecord(tmr_timezone=tz, tmr_current_time=ct, tmr_sunrise=sr, \
		tmr_sunset=ss, tmr_temperature=temp, tmr_feels_like=fl, tmr_pressure=press, tmr_humidity=hum, tmr_weather_main=wm,\
		tmr_description=desc)]
	sess.add(city)
	sess.commit()
	return True