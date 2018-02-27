#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'A simple service to get cpuinfo as an example of using swagger -2.0 specification and codegen'})
    app.run(port=8080)
