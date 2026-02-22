# About
This is the repo for my custom 60% mechanical keyboard powered by a Raspberry pi pico and KMK firmware I designed and built during Hackclub's [Blueprint program](https://blueprint.hackclub.com/home)
# Keys
My keyboard is a 60% keyboard with 60 keys and a rotary encoder used for volume and brightness control.

Here is the link to my [keyboard layout](https://www.keyboard-layout-editor.com/#/gists/8c5516ec0065e4f4e203846337e67ee0) (the ENC placeholder bottom right is where the rotary encoder goes)

My spacebar, left shift, right shift, enter and backspace all need MX stabilizers that I will solder onto the PCB as they are all above 2u.

| Key | Size | Stabilizer |
|-----|------|------------|
|Space| 6.25u| 6.25u PCB  |
|L-Shift| 2.25u | 2u PCB |
|R-Shift| 2.75u | 2u PCB |
|Enter | 2.25u | 2u PCB |
|Backspace | 2u | 2u PCB |



# BOM
| Qty | Item | Notes | Cost (£) | USD ($) | Link |
|------|-----|-------|----------|---------|------|
| 60 | MX-Style key switches | Black 70pcs | £13.50 | $18.20 | [AE](https://www.aliexpress.com/item/1005006255961111.html?spm=a2g0o.productlist.main.6.1c5fx2Aix2AiWV&algo_pvid=4bd67d72-8148-4282-8734-cf3fe3826a11&algo_exp_id=4bd67d72-8148-4282-8734-cf3fe3826a11-5&pdp_ext_f=%7B%22order%22%3A%222131%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%214.57%210.76%21%21%2141.14%216.86%21%40211b876e17717677747494032e62e8%2112000036489552472%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895%3BpisId%3A5000000197842856&curPageLogUid=AYo0klr2EJoX&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006255961111%7C_p_origin_prod%3A)
| 126 | Cherry MX Key caps | Yunhu White | £1.63 | $2.20 | [AE](https://www.aliexpress.com/item/1005007321700850.html) |
| 1 | Raspberry Pi Pico | WH | £5.40 | $7.28 | [PiHut](https://thepihut.com/products/raspberry-pi-pico-2?variant=54063366701441) |
| 5 | EC11 Rotary Encoder | With switch | £2.59 | $3.49 | [AE](https://www.aliexpress.com/item/32759396738.html?spm=a2g0o.productlist.main.2.63062NPL2NPLMO&algo_pvid=63e5fc57-c172-46cd-934d-df30d945a5f3&algo_exp_id=63e5fc57-c172-46cd-934d-df30d945a5f3-1&pdp_ext_f=%7B%22order%22%3A%2291%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%212.59%212.59%21%21%213.38%213.38%21%40211b612517717664069831568eee59%2112000038049525232%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895&curPageLogUid=noCgrMLyl2R2&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A32759396738%7C_p_origin_prod%3A) |
| 5 | Plate-mount stabilizers | 4x 2u and 6.25u - A3| £1.89 | $2.55 | [AE](https://www.aliexpress.com/item/1005007212869086.html) |
| 100 | 1N4148 diodes | Through-hole | £0.76 | $1.02 | [AE](https://www.aliexpress.com/item/4001126137167.html?spm=a2g0o.productlist.main.1.90b1o1uho1uh6B&algo_pvid=c367e696-c97b-45f9-aadc-442c0813800d&algo_exp_id=c367e696-c97b-45f9-aadc-442c0813800d-0&pdp_ext_f=%7B%22order%22%3A%221197%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%210.89%210.76%21%21%211.16%210.99%21%402103894417717723958752301e1008%2110000014629985518%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac7b67d0a%3Bm03_new_user%3A-29895%3BpisId%3A5000000197842856&curPageLogUid=KHdyO7FyLrgo&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A4001126137167%7C_p_origin_prod%3A) |
| 50 | Rubber feet pads | 13x5.5mm | £0.76 | $1.02 | [AE](https://www.aliexpress.com/item/1005006832476105.html) |
| 5 | Custom PCB | (Quote estimate) | £ | $ | [JLCPCB]([https://www.aliexpress.com/item/1005006832476105.html](https://jlcpcb.com/)) |
| **352** | **Total cost:** | **Not counting shipping** | **£29.68** | **$40.01** | [BOM](/Bom.md) |



| 60 | MX-Style key switches | AliExpress | £ | $ | [AE]() |


# Full Wiring Table

|  Net | GPIO | Notes |
|------|------|-------|
| ROW0 | GP2| Matrix  |
| ROW1 | GP3 | Matrix |
| ROW2 | GP4 | Matrix |
| ROW3 | GP5 | Matrix |
| ROW4 | GP6 | Matrix |
| COL0 | GP7 | Matrix  |
| COL1 | GP8 | Matrix |
| COL2 | GP9 | Matrix |
| COL3 | GP10 | Matrix |
| COL4 | GP11 | Matrix |
| COL5 | GP12 | Matrix |
| COL6 | GP13 | Matrix |
| ENC_A | GP16 | Rot A |
| ENC_B | GP17 | Rot B |
| ENC_SW | GP18 | Switch |
| GND | GND | Ground |
| +3V3 | 3V3 | Pico Pin |
| GND | GND | Common |
