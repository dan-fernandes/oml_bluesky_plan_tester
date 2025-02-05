from enum import Enum


class Plans(Enum):
    BIMORPH_OPTIMISATION = "bimorph_optimisation"


def get_plan(plan_name: Plans):
    """Util function to return Bluesky plan with given name.

    Args:
        plan_name: str name of plan to return

    Returns:
        A Bluesky plan
    """
    match plan_name:
        case Plans.BIMORPH_OPTIMISATION:
            from dodal.plans.bimorph import bimorph_optimisation

            return bimorph_optimisation
