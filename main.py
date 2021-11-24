def on_button_pressed_a():
    led.enable(False)
    basic.pause(500)
    OLED12864_I2C.show_string(0, 0, "Temperature", 1)
    OLED12864_I2C.show_number(3, 2, dht11.temperature(), 1)
    basic.pause(1000)
    OLED12864_I2C.clear()
    WiFiBit.execute_http_method(HttpMethod.GET,
        "api.thingspeak.com",
        80,
        "/update?api_key=15OV21L5P9CGEUFT&field1=" + ("" + str(dht11.temperature())),
        "")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    led.enable(False)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    led.enable(False)
    if dht11.humidity() >= 50:
        for index in range(6):
            pins.digital_write_pin(DigitalPin.P1, 1)
            basic.pause(200)
            pins.digital_write_pin(DigitalPin.P1, 0)
            basic.pause(200)
    elif dht11.humidity() < 50:
        for index2 in range(6):
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(200)
            pins.digital_write_pin(DigitalPin.P2, 0)
            basic.pause(200)
    OLED12864_I2C.show_string(0, 0, "Humidity", 1)
    OLED12864_I2C.show_number(3, 2, dht11.humidity(), 1)
    basic.pause(1000)
    OLED12864_I2C.clear()
    WiFiBit.execute_http_method(HttpMethod.GET,
        "api.thingspeak.com",
        80,
        "/update?api_key=15OV21L5P9CGEUFT&field2=" + ("" + str(dht11.humidity())),
        "")
input.on_button_pressed(Button.B, on_button_pressed_b)

dht11.set_pin(DigitalPin.P0)
OLED12864_I2C.init(60)
WiFiBit.connect_to_wi_fi_bit()
WiFiBit.connect_to_wi_fi_network("INS-M2000-61DE", "88908431")
OLED12864_I2C.clear()

def on_forever():
    pass
basic.forever(on_forever)
