import asyncio

import fastapi.routing

from app.internal.constant.models import UpdateConstantsRequest
from app.internal.constant.usecase import ConstantUseCase


class ConstantHandler:
    __const_uc: ConstantUseCase

    router: fastapi.routing.APIRouter

    def __init__(self, const_uc):
        self.__const_uc = const_uc
        self.router = fastapi.routing.APIRouter(prefix="/constant")

        self.router.add_api_route("/", self.get)
        self.router.add_api_route("/industries", self.get_industries)
        self.router.add_api_route("/fields", self.get_fields)
        self.router.add_api_route("/update", self.update_constants, methods=["PATCH"])
        self.router.add_api_route("/new", self.insert_constants, methods=["POST"])

    async def get(self):
        return await self.__const_uc._async_get_data()

    async def get_industries(self):

        return await self.__const_uc.get_industries()

    async def get_fields(self):
        return await self.__const_uc.get_fields()

    async def update_constants(self, params: UpdateConstantsRequest) -> dict:
        await self.__const_uc.update_constants(params)
        return {
            "internal_code": 200,
            "message": "successfully updated constants"
        }

    async def insert_constants(self, params: UpdateConstantsRequest) -> dict:
        await self.__const_uc.insert_constants(params)
        return {
            "internal_code": 200,
            "message": "successfully updated constants"
        }

