from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, P
from ...predicates import ChildPredicates

app_label = 'flourish_child'
pc = ChildPredicates()


@register()
class ChildGAD7ReferralRuleGroup(CrfRuleGroup):

    gad_anxiety_referral = CrfRule(
        predicate=P('referred_to', 'eq', 'receiving_emotional_care'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.childgadreferralfu'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.childgadreferral'
