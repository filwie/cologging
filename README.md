# cologging
## Description
Add some colors to your logs in one simple step!

## Quickstart
- Add the formatter to your stream handler and enjoy rainbowy output
``` python
import cologging
import logging

log = logging.getLogger('Colorful')

formatter = cologging.ColorFormatter('%(levelname)s: %(message)s')

sh = logging.StreamHandler()
sh.setFormatter(formatter)

log.addHandler(sh)
log.setLevel(logging.DEBUG)

log.debug('Debug in blue')
log.info('Info in green')
log.warning('Warning in yellow')
log.error('Error in red')
```

- As you can see the colors are not added when output is redirected
<img src="https://raw.githubusercontent.com/filwie/images/master/cologging/demo.png" alt="demo" width="100%"/>
