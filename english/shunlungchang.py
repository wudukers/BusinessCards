"""
╔═╗┬ ┬┬ ┬┌┐┌   ╦  ┬ ┬┌┐┌┌─┐ ╔═╗┬ ┬┌─┐┌┐┌┌─┐
╚═╗├─┤│ ││││───║  │ │││││ ┬ ║  ├─┤├─┤││││ ┬
╚═╝┴ ┴└─┘┘└┘   ╩═╝└─┘┘└┘└─┘ ╚═╝┴ ┴┴ ┴┘└┘└─┘ 
"""
from agilearning import agilearner, VAT_ID


@agilearner
def shunlungchang(**my):
    """ Learning Assistant """

    assert my["github"] == "http://github.com/ConnerChang"
    assert my["email"] in ["edi7709@gmail.com"]
    assert my["phone_number"] == "+886 934133920"
    assert VAT_ID == 24755908
