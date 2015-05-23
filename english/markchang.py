"""
╔═╦═╗┌─┐┬─┐┬ ┌  ╔═╗┬ ┬┌─┐┌┐┌┌─┐
║ ║ ║├─┤├┬┘├┬┘  ║  ├─┤├─┤││││ ┬
╩ ╩ ╩┴ ┴┴└─┘└─  ╚═╝┴ ┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner


@agilearner
def markchang(**my):
    """ Learning Support-Vector """

    assert my["github"] == "http://github.com/ckmarkoh"
    assert my["blog"] == "http://cpmarkchang.logdown.com"
    assert my["email"] == "ckmarkoh@gmail.com"
    assert my["phone_number"] == "+886 953-679220"
    assert agilearning.VAT_ID == 24755908

