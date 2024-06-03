import openpyxl
from openpyxl.xml.functions import QName, fromstring

HLSMAX = 240
RGBMAX = 255


def get_theme_colors(wb):
    xlmns = 'http://schemas.openxmlformats.org/drawingml/2006/main'
    root = fromstring(wb.loaded_theme)
    themeEl = root.find(QName(xlmns, 'themeElements').text)
    colorSchemes = themeEl.findall(QName(xlmns, 'clrScheme').text)
    firstColorScheme = colorSchemes[0]

    colors = []

    for c in ['lt1', 'dk1', 'lt2', 'dk2', 'accent1', 'accent2', 'accent3', 'accent4', 'accent5', 'accent6']:
        accent = firstColorScheme.find(QName(xlmns, c).text)

        if 'window' in accent.getchildren()[0].attrib['val']:
            colors.append(accent.getchildren()[0].attrib['lastClr'])
        else:
            colors.append(accent.getchildren()[0].attrib['val'])

    return colors


def rgb_to_ms_hls(red, green=None, blue=None):
    if green is None:
        if isinstance(red, str):
            if len(red) > 6:
                red = red[-6:]
            blue = int(red[4:], 16)
            green = int(red[2:4], 16)
            red = int(red[0:2], 16)
        else:
            blue = red[2]
            green = red[1]
            red = red[0]

    c_max, c_min = (max(red, green, blue), min(red, green, blue))
    c_diff, c_sum = c_max - c_min, c_max + c_min
    c_avg = c_sum // 2

    lightness = (c_sum * HLSMAX + RGBMAX) // (2 * RGBMAX)

    if c_max == c_min:
        saturation = 0
        hue = HLSMAX * 2 // 3
    else:
        if lightness <= HLSMAX // 2:
            saturation = ((c_diff * HLSMAX) + c_avg) // c_sum
        else:
            saturation = ((c_diff * HLSMAX) + ((2 * RGBMAX - c_sum) // 2)) // (2 * RGBMAX - c_sum)

    Rdelta = (((c_max - red) * (HLSMAX // 6)) + c_avg) // c_diff
    Gdelta = (((c_max - green) * (HLSMAX // 6)) + c_avg) // c_diff
    Bdelta = (((c_max - blue) * (HLSMAX // 6)) + c_avg) // c_diff

    if (red == c_max):
        hue = Bdelta - Gdelta
    elif (green == c_max):
        hue = (HLSMAX // 3) + Rdelta - Bdelta
    else:  # B == c_max
        hue = ((2 * HLSMAX) // 3) + Gdelta - Rdelta

    if (hue < 0):
        hue = hue + HLSMAX
    if (hue > HLSMAX):
        hue = hue - HLSMAX

    return (hue, lightness, saturation)


def rgb_to_hex(red, green=None, blue=None):
    if green is None:
        red, green, blue = red
    return ('%02x%02x%02x' % (red, green, blue)).upper()


def ms_hue_to_col(m1, m2, hue):
    if hue < 0:
        hue = hue + HLSMAX
    elif hue > HLSMAX:
        hue = hue - HLSMAX

    md = m2 - m1
    # return r,g, or b value from this tridrant
    if hue < HLSMAX // 6:
        return m1 + ((md * hue + (HLSMAX // 12)) // (HLSMAX // 6))
    elif hue < HLSMAX // 2:
        return m2
    elif hue < HLSMAX * 2 // 3:
        return m1 + ((md * ((HLSMAX * 2 // 3) - hue) + HLSMAX // 12) // (HLSMAX // 6))
    else:
        return m1


def ms_hls_to_rgb(hue, lightness=None, saturation=None):
    if lightness is None:
        hue, lightness, saturation = hue

    if saturation == 0:
        red = lightness * RGBMAX // HLSMAX
        green = red
        blue = red
    else:
        if lightness <= HLSMAX // 2:
            m2 = (lightness * (HLSMAX + saturation) + HLSMAX // 2) // HLSMAX
        else:
            m2 = lightness + saturation - ((lightness * saturation) + HLSMAX // 2) // HLSMAX
        m1 = 2 * lightness - m2

        red = (ms_hue_to_col(m1, m2, hue + HLSMAX // 3) * RGBMAX + HLSMAX // 2) // HLSMAX
        green = (ms_hue_to_col(m1, m2, hue) * RGBMAX + HLSMAX // 2) // HLSMAX
        blue = (ms_hue_to_col(m1, m2, hue - HLSMAX // 3) * RGBMAX + HLSMAX // 2) // HLSMAX
    return (red, green, blue)


def tint_luminance(tint, lum):
    if tint < 0:
        return int(round(lum * (1.0 + tint)))
    else:
        return int(round(lum * (1.0 - tint) + (HLSMAX - HLSMAX * (1.0 - tint))))


def theme_and_tint_to_rgb(wb, theme, tint):
    rgb = get_theme_colors(wb)[theme]
    h, l, s = rgb_to_ms_hls(rgb)
    return rgb_to_hex(ms_hls_to_rgb(h, tint_luminance(tint, l), s))


# Đường dẫn đến file Excel
file_path = r"C:\Users\KNT21617\Downloads\newken\project\data\raw\input.xlsx"

# Mở workbook
wb = openpyxl.load_workbook(file_path)
# Lấy sheet đầu tiên
sheet = wb.active

# Duyệt qua tất cả các ô trong sheet
for row in sheet.iter_rows():
    for cell in row:
        # fill = cell.fill
        # if fill.start_color.index != '00000000':
        #     print(f"Cell {cell.coordinate} has background color: {fill.start_color.index}")
        theme = cell.fill.start_color.theme
        tint = cell.fill.start_color.tint
        color = theme_and_tint_to_rgb(wb, theme, tint)
        print(color)
# Đóng workbook
wb.close()
