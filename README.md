# Prometheus exporter for Netatmo Healthy Homecoach.

## Running

The Docker image is available at https://hub.docker.com/r/djetelina/netatmo-homecoach-prometheus-exporter

Requires the following ENV variables:
* `CLIENT_ID` and `CLIENT_SECRET` of your netatmo application (create one through netatmo dev portal).
* `USERNAME` and `PASSWORD` for your netatmo account to which your healthcoch is registered.

Prometheus metrics are available on `localhost:5000`.

Version 1.0 supports exporting only the first health coach returned by Netatmo API. If you have multiple, wait for 2.0.

The exporter does **NOT** need to run on the same network as your Healthcoach, data is available through an external Netatmo API.

## Exported metrics

* Gauge `homecoach_temperature` - temperature (in °C)
* Gauge `homecoach_co2` - CO2 level (in ppm)
* Gauge `homecoach_humidity` - humidity (in %)
* Gauge `homecoach_noise` - noise (in dB)
* Gauge `homecoach_pressure` - surface pressure in mbar
* Gauge `homecoach_absolute_pressure` - sea-level pressure in mbar
* Gauge `homecoach_health_index` - health_index
