
import flet
from flet import (AlertDialog, Column, ElevatedButton, Icon, IconButton, Page,
                  Row, Text, TextButton, TextField, colors, icons)
from flet.buttons import ButtonStyle, RoundedRectangleBorder


def main(page: Page):
    page.title = "Web3 Fit"
    page.vertical_alignment = "center"
    page.window_min_height = 600
    page.window_min_width = 400
    page.design = "adaptive"
    page.scroll = "hidden"
    # page.window_frameless = True

    def do_maths(e):
        pass
    
    def connect_account(e):
        pass

    def get_fit_data(e):
        pass

    def claim_rewards(e):
        pass

    def closeclaim_dlg(e):
        claim_dlg.open = False
        page.update()

    def show_dlg(e):
        page.dialog = claim_dlg
        claim_dlg.open = True
        page.update()
        # time.sleep(5)
        # close_dlg()
        pass


    addr = TextField(label="enter wallet address", icon=icons.EMOJI_EMOTIONS)
    wbtn = TextButton("withdraw", on_click=closeclaim_dlg)

    avt = IconButton(content=Icon(icons.RUN_CIRCLE_ROUNDED, size=200, color=colors.BLUE_600), 
    style=ButtonStyle(
        elevation={"pressed": 0, "": 7},
        bgcolor={"hovered": colors.BLUE_100, "pressed": colors.BLUE_300},), on_click=get_fit_data)

    heart_points = Text("1 000 000", size=20, color=colors.BLUE_600,weight="w100")
    htxt = Text("Heart Pts", size=20)
    
    steps = Text("1 000 000", size=20, color=colors.BLUE_600,weight="w100")
    stxt = Text("Steps", size=20)

    cal = Text("2 000 000", size=20, color=colors.BLUE_600,weight="w100")
    ctxt = Text("Cal", size=20)

    km = Text("3 000 000", size=20, color=colors.BLUE_600,weight="w100")
    ktxt = Text("km", size=20)

    move_min = Text("3 000 000", size=20, color=colors.BLUE_600,weight="w100")
    mtxt = Text("Move Min", size=20)

    earning = Text("Earning\n1000 XRP")

    googl = IconButton(content=Icon(icons.CONNECT_WITHOUT_CONTACT_ROUNDED, size=50, color=colors.BLUE_200),
    style=ButtonStyle(
        elevation={"pressed": 0, "": 7},
        bgcolor={"pressed": colors.BLUE_500}), on_click=get_fit_data)

    claim = ElevatedButton(text="Claim Rewards", style=ButtonStyle(
        shape={"": RoundedRectangleBorder(radius=5)}, 
        elevation={"pressed": 0, "": 7},
    ),width=300, height=50, on_click=show_dlg, icon=icons.ATTACH_MONEY_ROUNDED, icon_color=colors.BLUE_ACCENT_100)

    claim_dlg = AlertDialog(
        # modal=True,
        title=Text("Withdrawal"),
        content=Text("Please input wallet adress"),
        actions=[
            addr,
            wbtn
        ],
        actions_alignment="end")

    notenough_dlg = AlertDialog(title=Text("Insufficient XRP to withdraw"), )

    page.add(
        Row([googl, Column(spacing=50) ,earning], alignment="end"),

        Row([avt],alignment="center"),
        Row(height=18),

        Row([heart_points, steps],alignment="center", spacing=50),
        Row([htxt, stxt], alignment="center", spacing=75),
        Row(height=18),

        Row([cal, km, move_min],alignment="center", spacing=50),
        Row([ctxt, ktxt, mtxt], alignment="center", spacing=85),
        Row(height=25),

        Row([claim], alignment="center")
    )

flet.app(port=58841, target=main)
