from inspect import isclass, isfunction, ismethod, ismodule

def test_experiment_dates(nt_user_date, rd_dart_experiment_date):
    """ Checks the business rules surrounding experiment dates.

    **Rule 1.** The dates should be within 4 hours of each other:
    >>> test_experiment_dates('2022-04-03 13:00', '2022-04-03 15:00')
    >>> test_experiment_dates('2022-04-03 13:00', '2022-04-30 15:00')
    Traceback (most recent call last):
        ...
    AssertionError: 00E302

    **Rule 2.** The NIH Toolbox (`nt_user_date`) should only happen on Tuesdays.
    >>> test_experiment_dates('2022-04-05 13:00', '2022-04-05 15:00')
    >>> test_experiment_dates('2022-04-06 13:00', '2022-04-06 15:00')
    Traceback (most recent call last):
        ...
    AssertionError: 00E303

    ℹ  Regarding the example dates above **04-03** = Sun, **04-05** = Tues, **04-06** = Wed


    """
    from datetime import timedelta, datetime

    a = datetime.fromisoformat(nt_user_date)
    b = datetime.fromisoformat(rd_dart_experiment_date)

    assert abs(a - b) < timedelta(hours=4), dict(
        code = "00E302",
        msg = "The two timestamps are greater than 4 hours"
    )

    assert a.weekday() == 1, dict(
        code = "00E303",
        msg = "The participant should only do Toolbox data on Tuesdays. IRB-requirement",
        priority = "critical",
        assign = "moisesbaltazar",
        watchers = ["mhodge01", "plenzini"],
    )

def test_valid_email(rd_email):
    """Checks that the email is in a valid format.

    ## Example valid email
    >>> test_valid_email("a@b.com")
    >>> test_valid_email("a.b@b.edu")
    >>> test_valid_email("a.b+c@b.cc")

    ## Invalid Emails
    >>> test_valid_email("z@b.c")
    Traceback (most recent call last):
        ...
    AssertionError: 00E304
    >>> test_valid_email("z!!!@b.com")
    Traceback (most recent call last):
        ...
    AssertionError: 00E304
    """
    assert not rd_email.startswith("z"), dict(
        code = "00E304",
        msg = "The participant's email is invalid."

    )
