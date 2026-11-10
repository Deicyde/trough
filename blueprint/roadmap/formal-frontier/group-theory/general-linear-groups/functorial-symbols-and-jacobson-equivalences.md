---
declaration: theorem
origin: cited
lean: Ideal.principalUnitsPowLayerSymbol_map, Ideal.powLayerMap_commutator, Ideal.principalUnitsPowLayerMap_commutator, Ideal.principalUnitsPowLayerEquiv, Ideal.principalUnitsPowLayerEquiv_symm_map, Ideal.principalUnitsPowLayerSymbol_surjective_of_forall_isNilpotent, Ideal.principalUnitsPowLayerSymbol_surjective_of_pow_eq_bot
statement: formalized
---

# Functorial symbols and Jacobson equivalences

On positive layers, unital ring maps carrying left ideals into left ideals induce integer-linear maps preserving symbols and commutator pairings, while Jacobson-contained ideals have symbol equivalences with natural inverses when both ideals satisfy the radical condition, and pointwise-nil or power-nilpotent left ideals have surjective symbols.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.principalUnitsPowLayerSymbol_map` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/Naturality.lean, line 120](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L120).
- `Ideal.powLayerMap_commutator` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/Naturality.lean, line 134](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L134).
- `Ideal.principalUnitsPowLayerMap_commutator` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/Naturality.lean, line 149](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L149).
- `Ideal.principalUnitsPowLayerEquiv` (def), declared in [GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean, line 61](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L61).
- `Ideal.principalUnitsPowLayerEquiv_symm_map` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean, line 135](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L135).
- `Ideal.principalUnitsPowLayerSymbol_surjective_of_forall_isNilpotent` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean, line 100](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L100).
- `Ideal.principalUnitsPowLayerSymbol_surjective_of_pow_eq_bot` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean, line 119](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L119).

Read from the source at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), without running Lean.

## Sources

- [general-linear-groups at a2199cf0: formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml)
- [Source of `Ideal.principalUnitsPowLayerSymbol_map` in GeneralLinearGroups/PrincipalUnits/Naturality.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L120)
- [Source of `Ideal.powLayerMap_commutator` in GeneralLinearGroups/PrincipalUnits/Naturality.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L134)
- [Source of `Ideal.principalUnitsPowLayerMap_commutator` in GeneralLinearGroups/PrincipalUnits/Naturality.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean#L149)
- [Source of `Ideal.principalUnitsPowLayerEquiv` in GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L61)
- [Source of `Ideal.principalUnitsPowLayerEquiv_symm_map` in GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L135)
- [Source of `Ideal.principalUnitsPowLayerSymbol_surjective_of_forall_isNilpotent` in GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L100)
- [Source of `Ideal.principalUnitsPowLayerSymbol_surjective_of_pow_eq_bot` in GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean#L119)
