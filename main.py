from nicegui import ui

class ColorModeButton(ui.button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._state = False
        self.on('click', self.toggle)

    def toggle(self) -> None:
        self._state = not self._state
        self.update()

    def update(self) -> None:
        self.props(f"color={'grey' if self._state else 'black'} icon={'light_mode' if self._state else 'dark_mode'}")
        if self._state:
            ui.dark_mode().disable()
        else:
            ui.dark_mode().enable()
        super().update()

def calculate_mrp():
    # Stools table
    stools_netto_need = int(order_quantity.value) - int(stools_supply.value)
    if stools_netto_need <= 0:
        stools_netto_need = 0
    if int(stools_supply.value) > int(order_quantity.value):
        supply_need = int(stools_supply.value) - int(order_quantity.value)
    else:
        supply_need = 0
    stools_rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': int(order_quantity.value)},
            {'id_col': 'Zapas', '1_col': int(stools_supply.value), '2_col': int(stools_supply.value), '3_col': int(stools_supply.value), '4_col': int(stools_supply.value), '5_col': int(stools_supply.value), '6_col': supply_need},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': stools_netto_need},
            {'id_col': 'Zlecenie produkcji', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': stools_netto_need if stools_netto_need else '-', '6_col': '-'},
    ]
    stools_table.update_rows(rows=stools_rows)
    
    # Upholstery table
    upholstery_netto_need = stools_netto_need * 0.5 - upholstery_supply.value
    if upholstery_netto_need <= 0:
        upholstery_netto_need = 0
    if upholstery_supply.value > stools_netto_need * 0.5:
        supply_need = upholstery_supply.value - stools_netto_need * 0.5
    else:
        supply_need = 0
    upholstery_rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': stools_netto_need * 0.5, '6_col': '-'},
            {'id_col': 'Zapas', '1_col': upholstery_supply.value, '2_col': upholstery_supply.value, '3_col': upholstery_supply.value, '4_col': upholstery_supply.value, '5_col': supply_need, '6_col': supply_need},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': upholstery_netto_need, '6_col': '-'},
            {'id_col': 'Zlecenie produkcji', '1_col': '-', '2_col': '-', '3_col': upholstery_netto_need if upholstery_netto_need else '-', '4_col': '-', '5_col': '-', '6_col': '-'},
    ]
    upholstery_table.update_rows(rows=upholstery_rows)

    # Seats table
    seats_netto_need = stools_netto_need - int(seats_supply.value)
    if seats_netto_need <= 0:
        seats_netto_need = 0
    if int(seats_supply.value) > stools_netto_need:
        supply_need = int(seats_supply.value) - stools_netto_need
    else:
        supply_need = 0
    seats_rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': stools_netto_need, '6_col': '-'},
            {'id_col': 'Zapas', '1_col': seats_supply.value, '2_col': seats_supply.value, '3_col': seats_supply.value, '4_col': seats_supply.value, '5_col': supply_need, '6_col': supply_need},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': seats_netto_need, '6_col': '-'},
            {'id_col': 'Zlecenie produkcji', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': seats_netto_need if seats_netto_need else '-', '5_col': '-', '6_col': '-'},
    ]
    seat_table.update_rows(rows=seats_rows)
    
    # Legs table
    legs_netto_need = seats_netto_need * 4 - int(legs_supply.value)
    if legs_netto_need <= 0:
        legs_netto_need = 0
    if int(legs_supply.value) > seats_netto_need * 4:
        supply_need = int(legs_supply.value) - seats_netto_need * 4
    else:
        supply_need = 0
    legs_rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': seats_netto_need * 4, '5_col': '-', '6_col': '-'},
            {'id_col': 'Zapas', '1_col': legs_supply.value, '2_col': legs_supply.value, '3_col': legs_supply.value, '4_col': supply_need, '5_col': supply_need, '6_col': supply_need},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': legs_netto_need, '5_col': '-', '6_col': '-'},
            {'id_col': 'Zlecenie produkcji', '1_col': legs_netto_need if legs_netto_need else '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': '-'},
    ]
    legs_table.update_rows(rows=legs_rows)

    # Wood table
    wood_netto_need = seats_netto_need - int(wood_supply.value)
    if wood_netto_need <= 0:
        wood_netto_need = 0
    if int(wood_supply.value) > seats_netto_need:
        supply_need = int(wood_supply.value) - seats_netto_need
    else:
        supply_need = 0
    wood_rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': seats_netto_need, '5_col': '-', '6_col': '-'},
            {'id_col': 'Zapas', '1_col': wood_supply.value, '2_col': wood_supply.value, '3_col': wood_supply.value, '4_col': supply_need, '5_col': supply_need, '6_col': supply_need},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': wood_netto_need, '5_col': '-', '6_col': '-'},
            {'id_col': 'Zlecenie produkcji', '1_col': '-', '2_col': '-', '3_col': wood_netto_need if wood_netto_need else '-', '4_col': '-', '5_col': '-', '6_col': '-'},
    ]
    wood_table.update_rows(rows=wood_rows)
    
rows = [
            {'id_col': 'Zapotrzebowanie brutto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': '-'},
            {'id_col': 'Zapas', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': '-'},
            {'id_col': 'Zapotrzebowanie netto', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': '-'},
            {'id_col': 'Zlecenie produkcji', '1_col': '-', '2_col': '-', '3_col': '-', '4_col': '-', '5_col': '-', '6_col': '-'},
]

stools_rows = rows.copy()
upholstery_rows = rows.copy()
seats_rows = rows.copy()
legs_rows = rows.copy()
wood_rows = rows.copy()

columns = [
            {'name': 'id_col', 'label': ' ', 'field': 'id_col', 'required': True, 'align': 'center'},
            {'name': '1_col', 'label': '1', 'field': '1_col', 'required': True, 'align': 'center'},
            {'name': '2_col', 'label': '2', 'field': '2_col', 'required': True, 'align': 'center'},
            {'name': '3_col', 'label': '3', 'field': '3_col', 'required': True, 'align': 'center'},
            {'name': '4_col', 'label': '4', 'field': '4_col', 'required': True, 'align': 'center'},
            {'name': '5_col', 'label': '5', 'field': '5_col', 'required': True, 'align': 'center'},
            {'name': '6_col', 'label': '6', 'field': '6_col', 'required': True, 'align': 'center'},
]

with ui.column().classes('w-full items-center'):
    with ui.row().classes('h-full justify-center'):
        with ui.card().classes('items-center').style('height: 500px;'):
            ui.markdown('## ⚙️ Konfiguracja:')
            ui.separator()
            ui.label('Zapasy:')
            with ui.row():
                legs_supply = ui.number(label='Nogi', value=0, min=0, suffix='szt.', format='%.f')
                wood_supply = ui.number(label='Drewniane okrągi', value=0, min=0, suffix='szt.', format='%.f')
            with ui.row():
                seats_supply = ui.number(label='Siedziska', value=0, min=0, suffix='szt.', format='%.f')
                upholstery_supply = ui.number(label='Obicie', value=0, min=0, suffix='mb.', step=0.5, format='%.1f')
            stools_supply = ui.number(label='Taborety', value=0, min=0, suffix='szt.', format='%.f').classes('w-full')
            ui.label('Zamówienie:')
            with ui.row():
                order_quantity = ui.number(label='Wielkość zamówienia:', value=1, min=1, suffix='szt.', format='%.f')
                ui.button('Oblicz', on_click=calculate_mrp)

        with ui.card().classes('items-center').style('height: 500px;'):
            ui.markdown('## 📆 Harmonogram MRP:')
            ui.separator()
            with ui.tabs().classes('w-full') as tabs:
                one = ui.tab('Taboret')
                two = ui.tab('Obicie')
                three = ui.tab('Siedzisko')
                four = ui.tab('Nogi')
                five = ui.tab('Drewniany okrąg')
            
            with ui.tab_panels(tabs, value=one).classes('w-full'):
                with ui.tab_panel(one).classes('items-center'):
                    stools_table = ui.table(columns=columns, rows=stools_rows, row_key='id_col')
                with ui.tab_panel(two).classes('items-center'):
                    upholstery_table = ui.table(columns=columns, rows=upholstery_rows, row_key='id_col')
                with ui.tab_panel(three).classes('items-center'):
                    seat_table = ui.table(columns=columns, rows=seats_rows, row_key='id_col')
                with ui.tab_panel(four).classes('items-center'):
                    legs_table = ui.table(columns=columns, rows=legs_rows, row_key='id_col')
                with ui.tab_panel(five).classes('items-center'):
                    wood_table = ui.table(columns=columns, rows=wood_rows, row_key='id_col')
        
        with ui.card().classes('items-center').style('height: 500px;'):
            ui.markdown('## 📋 Receptura produkcyjna:')
            ui.separator()
            ui.mermaid('''
            graph BT;
                A["`**Taboret**
                Ilość: _1 szt._
                Czas: _1 tyg._
                `"]
                B["`**Obicie**
                Ilość: _0,5 mb._
                Czas: _2 tyg._
                `"]
                C["`**Siedzisko**
                Ilość: _1 szt._
                Czas: _1 tyg._
                `"]
                D["`**Drewniany okrąg**
                Ilość: _1 szt._
                Czas: _1 tyg._
                `"]
                E["`**Nogi**
                Ilość: _4 szt._
                Czas: _3 tyg._
                `"]
                E --> C;
                D --> C;
                C --> A;
                B --> A;
            ''')

with ui.page_sticky(x_offset=18, y_offset=18):
    ColorModeButton()

ui.dark_mode().enable()
ui.run(title='System MRP', favicon='📦')