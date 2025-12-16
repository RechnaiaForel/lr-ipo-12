import dearpygui.dearpygui as dpg

def add_client_callback(sender, app_data):
    dpg.show_item("Client Window")

def add_vehicle_callback(sender, app_data):
    dpg.show_item("Transport Window")

def distribute_callback(sender, app_data):
    print("Optimizing cargo...")

dpg.create_context()

with dpg.window(label="Main Window", tag="Main Window"):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Export result", callback=lambda s, a: print("Export..."))
            dpg.add_menu_item(label="About", callback=lambda s, a: print("LR-12, variant 2, Dmitry"))

    dpg.add_button(label="Add client", callback=add_client_callback)
    dpg.add_button(label="Add vehicle", callback=add_vehicle_callback)
    dpg.add_button(label="Distribute cargo", callback=distribute_callback)

    dpg.add_text("Status: ready")

with dpg.window(label="Client Window", tag="Client Window", show=False):
    dpg.add_input_text(label="Client name")
    dpg.add_input_float(label="Cargo weight")
    dpg.add_checkbox(label="VIP status")
    dpg.add_button(label="Save client", callback=lambda s, a: print("Client saved"))
    dpg.add_button(label="Cancel", callback=lambda s, a: dpg.hide_item("Client Window"))

with dpg.window(label="Transport Window", tag="Transport Window", show=False):
    dpg.add_combo(label="Transport type", items=["Truck", "Ship"])
    dpg.add_input_float(label="Capacity")
    dpg.add_input_text(label="Color/Name")
    dpg.add_button(label="Save vehicle", callback=lambda s, a: print("Vehicle saved"))
    dpg.add_button(label="Cancel", callback=lambda s, a: dpg.hide_item("Transport Window"))

dpg.create_viewport(title='LR-12', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()