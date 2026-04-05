def is_point_in_triangle(x, y, a, b):
    # площі
    def area(x1,y1,x2,y2,x3,y3):
        return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)

    A = area(a,0, 0,b, 0,0)
    A1 = area(x,y, 0,b, 0,0)
    A2 = area(a,0, x,y, 0,0)
    A3 = area(a,0, 0,b, x,y)

    return A == A1 + A2 + A3


def translate(text, lang):
    ua = {
        "inside": "належить трикутнику",
        "outside": "не належить трикутнику"
    }
    en = {
        "inside": "belongs to triangle",
        "outside": "does not belong to triangle"
    }
    return ua[text] if lang != "en" else en[text]