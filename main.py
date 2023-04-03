import api.calculator_api as api

import uvicorn
uvicorn.run(api.app, host="0.0.0.0", port=8000)

x = 2
