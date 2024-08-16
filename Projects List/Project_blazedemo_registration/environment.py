def before_all(context):
   context.driver.setup_driver(context)

def after_all(context):
    context.driver.quit()