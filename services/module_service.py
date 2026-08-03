import json

from database.config import SessionLocal
from database.models import Module


class ModuleService:

    def save(self, module_name, variables, dependencies):

        db = SessionLocal()

        module = Module(
            module_name=module_name,
            variables=json.dumps(variables),
            dependencies=json.dumps(dependencies)
        )

        db.add(module)
        db.commit()
        db.close()