import os
from hamcrest import assert_that, equal_to, is_not
#komenda ="cat /proc/cpuinfo | grep 'cpu core' | wc -l"
@given(u'otwieram terminal')
def step_impl(context):
    context.os=os
#    raise NotImplementedError(u'STEP: Given otwieram terminal')

@when(u'wpisuje komende')
def step_impl(context):
    wynik = os.popen("cat /proc/cpuinfo | grep 'cpu core' | wc -l").read()
    context.wynik = wynik
    #raise NotImplementedError(u'STEP: When wpisuje komende')


@then(u'otrzymuje wynik')
def step_impl(context):
    print context.wynik
    assert_that(int(context.wynik), equal_to(8968900))
    #raise NotImplementedError(u'STEP: Then otrzymuje wynik')
