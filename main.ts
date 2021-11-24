input.onButtonPressed(Button.A, function () {
    OLED12864_I2C.showString(
    0,
    0,
    "Temperature",
    1
    )
    OLED12864_I2C.showNumber(
    3,
    2,
    dht11_dht22.readData(dataType.temperature),
    1
    )
    basic.pause(1000)
    OLED12864_I2C.clear()
    WiFiBit.executeHttpMethod(
    HttpMethod.GET,
    "api.thingspeak.com",
    80,
    "/update?api_key=15OV21L5P9CGEUFT&field1=" + ("" + dht11_dht22.readData(dataType.temperature)),
    ""
    )
})
input.onButtonPressed(Button.B, function () {
    if (pins.analogReadPin(AnalogPin.P0) >= 100) {
        pins.digitalWritePin(DigitalPin.P13, 1)
        basic.pause(1000)
        pins.digitalWritePin(DigitalPin.P13, 0)
    } else if (pins.analogReadPin(AnalogPin.P0) < 100) {
        pins.digitalWritePin(DigitalPin.P14, 1)
        basic.pause(1000)
        pins.digitalWritePin(DigitalPin.P14, 0)
    }
    led.enable(false)
    OLED12864_I2C.showString(
    0,
    0,
    "Humidity",
    1
    )
    OLED12864_I2C.showNumber(
    3,
    2,
    dht11_dht22.readData(dataType.humidity),
    1
    )
    basic.pause(1000)
    OLED12864_I2C.clear()
    WiFiBit.executeHttpMethod(
    HttpMethod.GET,
    "api.thingspeak.com",
    80,
    "/update?api_key=15OV21L5P9CGEUFT&field2=" + ("" + dht11_dht22.readData(dataType.humidity)),
    ""
    )
})
dht11_dht22.queryData(
DHTtype.DHT11,
DigitalPin.P0,
true,
false,
true
)
OLED12864_I2C.init(60)
WiFiBit.connectToWiFiBit()
WiFiBit.connectToWiFiNetwork("MyWifiSSID", "Password")
OLED12864_I2C.clear()
