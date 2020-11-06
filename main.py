noise = 0
light2=0
led.enable(False)
strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)

def on_forever():
    global noise
    light2 = smarthome.read_light_intensity(AnalogPin.P3)
    if light2 < 50:
        noise = smarthome.read_noise(AnalogPin.P2)

    
        if noise > 70:
            strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
            basic.pause(10000)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
basic.forever(on_forever)
