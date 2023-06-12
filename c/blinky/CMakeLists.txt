cmake_minimum_required(VERSION 3.13)

# initialize the SDK
# note: this must happen before project()
include(../pico-sdk/pico_sdk_init.cmake)

project(my_project)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

# rest of your project
add_executable(blinky
        blinky.c
        )

target_link_libraries(blinky
        pico_stdlib              # for core functionality
        pico_cyw43_arch_none     # we need Wifi to access the GPIO, but we don't need anything else
        )

# create map/bin/hex file etc.
pico_add_extra_outputs(blinky)
