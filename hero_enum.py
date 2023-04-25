import random
from enum import Enum
from typing import List


class RoleEnum(Enum):
    TANK = "Tank"
    DPS = "Damage"
    SUPPORT = "Support"

    @property
    def color(self):
        match self:
            case RoleEnum.TANK:
                return "E8D44F"
            case RoleEnum.DPS:
                return "B43E3E"
            case RoleEnum.SUPPORT:
                return "218FFE"


class HeroEnum(Enum):
    ANA = "Ana"
    ASHE = "Ashe"
    BAPTISTE = "Baptiste"
    BASTION = "Bastion"
    BRIGITTE = "Brigitte"
    CASSIDY = "Cassidy"
    D_VA = "D.va"
    DOOMFIST = "Doomfist"
    ECHO = "Echo"
    GENJI = "Genji"
    HANZO = "Hanzo"
    JUNKER_QUEEN = "Junker Queen"
    JUNKRAT = "Junkrat"
    KIRIKO = "Kiriko"
    LIFEWEAVER = "Lifeweaver"
    LUCIO = "Lucio"
    MEI = "Mei"
    MERCY = "Mercy"
    MOIRA = "Moira"
    ORISA = "Orisa"
    PHARAH = "Pharah"
    RAMATTRA = "Ramattra"
    REAPER = "Reaper"
    REINHARDT = "Reinhardt"
    ROADHOG = "Roadhog"
    SIGMA = "Sigma"
    SOJOURN = "Sojourn"
    SOLDIER_76 = "Soldier 76"
    SOMBRA = "Sombra"
    SYMMETRA = "Symmetra"
    TORBJORN = "Torbjorn"
    TRACER = "Tracer"
    WIDOWMAKER = "Widowmaker"
    WINSTON = "Winston"
    WRECKING_BALL = "Wrecking Ball"
    ZARYA = "Zarya"
    ZENYATTA = "Zenyatta"

    @classmethod
    def random_hero(cls) -> "HeroEnum":
        return random.choice([e for e in cls])

    @classmethod
    def support_heroes(cls) -> List["HeroEnum"]:
        return HERO_ROLE_MAPPING[RoleEnum.SUPPORT]

    @classmethod
    def random_support(cls) -> "HeroEnum":
        return random.choice(cls.support_heroes())

    @classmethod
    def damage_heroes(cls) -> List["HeroEnum"]:
        return HERO_ROLE_MAPPING[RoleEnum.DPS]

    @classmethod
    def random_dps(cls) -> "HeroEnum":
        return random.choice(cls.damage_heroes())

    @classmethod
    def tank_heroes(cls) -> List["HeroEnum"]:
        return HERO_ROLE_MAPPING[RoleEnum.TANK]

    @classmethod
    def random_tank(cls) -> "HeroEnum":
        return random.choice(cls.tank_heroes())

    # Instance properties
    @property
    def avatar_url(self) -> str:
        return AVATAR_URLS[self]

    @property
    def role(self) -> RoleEnum:
        for role, heroes in HERO_ROLE_MAPPING.items():
            if self in heroes:
                return role
        raise ValueError("Not all heroes have roles?")


HERO_ROLE_MAPPING = {
    RoleEnum.TANK: [
        HeroEnum.D_VA,
        HeroEnum.DOOMFIST,
        HeroEnum.JUNKER_QUEEN,
        HeroEnum.ORISA,
        HeroEnum.RAMATTRA,
        HeroEnum.REINHARDT,
        HeroEnum.ROADHOG,
        HeroEnum.SIGMA,
        HeroEnum.WINSTON,
        HeroEnum.WRECKING_BALL,
        HeroEnum.ZARYA,
    ],
    RoleEnum.DPS: [
        HeroEnum.ASHE,
        HeroEnum.BASTION,
        HeroEnum.CASSIDY,
        HeroEnum.ECHO,
        HeroEnum.GENJI,
        HeroEnum.HANZO,
        HeroEnum.JUNKRAT,
        HeroEnum.MEI,
        HeroEnum.PHARAH,
        HeroEnum.REAPER,
        HeroEnum.SOJOURN,
        HeroEnum.SOLDIER_76,
        HeroEnum.SOMBRA,
        HeroEnum.SYMMETRA,
        HeroEnum.TORBJORN,
        HeroEnum.TRACER,
        HeroEnum.WIDOWMAKER,
    ],
    RoleEnum.SUPPORT: [
        HeroEnum.ANA,
        HeroEnum.BAPTISTE,
        HeroEnum.BRIGITTE,
        HeroEnum.KIRIKO,
        HeroEnum.LIFEWEAVER,
        HeroEnum.LUCIO,
        HeroEnum.MERCY,
        HeroEnum.MOIRA,
        HeroEnum.ZENYATTA,
    ],
}


def assert_all_heroes_have_roles() -> None:
    all_heroes = {e for e in HeroEnum}
    all_role_heroes = {e for r, h in HERO_ROLE_MAPPING.items() for e in h}
    if all_heroes != all_role_heroes:
        raise ValueError(f"Not all heroes have roles: {all_heroes.difference(all_role_heroes)}")


assert_all_heroes_have_roles()


def avatar_url(value: str) -> str:
    return f"https://d15f34w2p8l1cc.cloudfront.net/overwatch/{value}.png"


AVATAR_URLS = {
    HeroEnum.ANA: avatar_url("3429c394716364bbef802180e9763d04812757c205e1b4568bc321772096ed86"),
    HeroEnum.ASHE: avatar_url("8dc2a024c9b7d95c7141b2ef065590dbc8d9018d12ad15f76b01923986702228"),
    HeroEnum.BAPTISTE: avatar_url("f979896f74ba22db2a92a85ae1260124ab0a26665957a624365e0f96e5ac5b5c"),
    HeroEnum.BASTION: avatar_url("4d715f722c42215072b5dd0240904aaed7b5285df0b2b082d0a7f1865b5ea992"),
    HeroEnum.BRIGITTE: avatar_url("48392820c6976ee1cd8dde13e71df85bf15560083ee5c8658fe7c298095d619a"),
    HeroEnum.CASSIDY: avatar_url("6cfb48b5597b657c2eafb1277dc5eef4a07eae90c265fcd37ed798189619f0a5"),
    HeroEnum.D_VA: avatar_url("ca114f72193e4d58a85c087e9409242f1a31e808cf4058678b8cbf767c2a9a0a"),
    HeroEnum.DOOMFIST: avatar_url("13750471c693c1a360eb19d5ace229c8599a729cd961d72ebee0e157657b7d18"),
    HeroEnum.ECHO: avatar_url("f086bf235cc6b7f138609594218a8385c8e5f6405a39eceb0deb9afb429619fe"),
    HeroEnum.GENJI: avatar_url("4edf5ea6d58c449a2aeb619a3fda9fff36a069dfbe4da8bc5d8ec1c758ddb8dc"),
    HeroEnum.HANZO: avatar_url("aecd8fa677f0093344fab7ccb7c37516c764df3f5ff339a5a845a030a27ba7e0"),
    HeroEnum.JUNKER_QUEEN: avatar_url("cef2406b2244b80506f83b8fb9ebaf214f41fa8795cbeef84026cd8018561d04"),
    HeroEnum.JUNKRAT: avatar_url("037e3df083624e5480f8996821287479a375f62b470572a22773da0eaf9441d0"),
    HeroEnum.KIRIKO: avatar_url("088aff2153bdfa426984b1d5c912f6af0ab313f0865a81be0edd114e9a2f79f9"),
    HeroEnum.LIFEWEAVER: avatar_url("39d4514f1b858bc228035b09d5a74ed41f8eeefc9a0d1873570b216ba04334df"),
    HeroEnum.LUCIO: avatar_url("e2ff2527610a0fbe0c9956f80925123ef3e66c213003e29d37436de30b90e4e1"),
    HeroEnum.MEI: avatar_url("1533fcb0ee1d3f9586f84b4067c6f63eca3322c1c661f69bfb41cd9e4f4bcc11"),
    HeroEnum.MERCY: avatar_url("2508ddd39a178d5f6ae993ab43eeb3e7961e5a54a9507e6ae347381193f28943"),
    HeroEnum.MOIRA: avatar_url("000beeb5606e01497897fa9210dd3b1e78e1159ebfd8afdc9e989047d7d3d08f"),
    HeroEnum.ORISA: avatar_url("71e96294617e81051d120b5d04b491bb1ea40e2933da44d6631aae149aac411d"),
    HeroEnum.PHARAH: avatar_url("f8261595eca3e43e3b37cadb8161902cc416e38b7e0caa855f4555001156d814"),
    HeroEnum.RAMATTRA: avatar_url("3e0367155e1940a24da076c6f1f065aacede88dbc323631491aa0cd5a51e0b66"),
    HeroEnum.REAPER: avatar_url("2edb9af69d987bb503cd31f7013ae693640e692b321a73d175957b9e64394f40"),
    HeroEnum.REINHARDT: avatar_url("490d2f79f8547d6e364306af60c8184fb8024b8e55809e4cc501126109981a65"),
    HeroEnum.ROADHOG: avatar_url("72e02e747b66b61fcbc02d35d350770b3ec7cbaabd0a7ca17c0d82743d43a7e8"),
    HeroEnum.SIGMA: avatar_url("cd7a4c0a0df8924afb2c9f6df864ed040f20250440c36ca2eb634acf6609c5e4"),
    HeroEnum.SOJOURN: avatar_url("a53bf7ad9d2f33aaf9199a00989f86d4ba1f67c281ba550312c7d96e70fec4ea"),
    HeroEnum.SOLDIER_76: avatar_url("20b4ef00ed05d6dba75df228241ed528df7b6c9556f04c8070bad1e2f89e0ff5"),
    HeroEnum.SOMBRA: avatar_url("bca8532688f01b071806063b9472f1c0f9fc9c7948e6b59e210006e69cec9022"),
    HeroEnum.SYMMETRA: avatar_url("7f2024c5387c9d76d944a5db021c2774d1e9d7cbf39e9b6a35b364d38ea250ac"),
    HeroEnum.TORBJORN: avatar_url("1309ab1add1cc19189a2c8bc7b1471f88efa1073e9705d2397fdb37d45707d01"),
    HeroEnum.TRACER: avatar_url("a66413200e934da19540afac965cfe8a2de4ada593d9a52d53108bb28e8bbc9c"),
    HeroEnum.WIDOWMAKER: avatar_url("a714f1cb33cc91c6b5b3e89ffe7e325b99e7c89cc8e8feced594f81305147efe"),
    HeroEnum.WINSTON: avatar_url("bd9c8e634d89488459dfc1aeb21b602fa5c39aa05601a4167682f3a3fed4e0ee"),
    HeroEnum.WRECKING_BALL: avatar_url("5c18e39ce567ee8a84078f775b9f76a2ba891de601c059a3d2b46b61ae4afb42"),
    HeroEnum.ZARYA: avatar_url("8819ba85823136640d8eba2af6fd7b19d46b9ee8ab192a4e06f396d1e5231f7a"),
    HeroEnum.ZENYATTA: avatar_url("71cabc939c577581f66b952f9c70891db779251e8e70f29de3c7bf494edacfe4"),
}
