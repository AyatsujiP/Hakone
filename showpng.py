import fitz
import svglib.svglib
import chess.svg
import io
from reportlab.graphics import renderPDF

def return_pngs():
    ret = []
    for piece in ["K","Q","R","B","N","P","k","q","r","b","n","p"]:
        svg_wk = svglib.svglib.svg2rlg(io.StringIO(chess.svg.piece(chess.Piece.from_symbol(piece))))
        pdf = renderPDF.drawToString(svg_wk)

        doc = fitz.Document(stream=pdf)
        png_tmp = doc.load_page(0).get_pixmap(alpha=True)
        r = io.BytesIO(png_tmp.tobytes())
        ret.append(r)
    return ret 