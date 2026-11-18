---
declaration: module
origin: cited
lean: StandardModel.repU1Map, StandardModel.repU1, StandardModel.fundamentalSU2, StandardModel.repU1_fundamentalSU2_commute
statement: formalized
proof: formalized
---

# Representations appearing in the Standard Model

The module `Physlib.Particles.StandardModel.Representations`, [Physlib/Particles/StandardModel/Representations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean): 4 declarations, 3 with a docstring.

> This file defines the basic representations which appear in the Standard Model.

**`StandardModel.repU1Map`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean#L28).

> The 2d representation of U(1) with charge 3 as a map from U(1) to `unitaryGroup (Fin 2) ℂ`.

```lean
noncomputable def repU1Map (g : unitary ℂ) : unitaryGroup (Fin 2) ℂ
```

**`StandardModel.repU1`**, a def, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean#L40).

> The 2d representation of U(1) with charge 3 as a homomorphism
> from U(1) to `unitaryGroup (Fin 2) ℂ`.

```lean
noncomputable def repU1 : unitary ℂ →* unitaryGroup (Fin 2) ℂ
```

**`StandardModel.fundamentalSU2`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean#L49).

> The fundamental representation of SU(2) as a homomorphism to `unitaryGroup (Fin 2) ℂ`.

```lean
def fundamentalSU2 : specialUnitaryGroup (Fin 2) ℂ →* unitaryGroup (Fin 2) ℂ
```

**`StandardModel.repU1_fundamentalSU2_commute`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean#L54).

```lean
lemma repU1_fundamentalSU2_commute (u1 : unitary ℂ) (g : specialUnitaryGroup (Fin 2) ℂ) :
    repU1 u1 * fundamentalSU2 g = fundamentalSU2 g * repU1 u1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Particles/StandardModel/Representations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Representations.lean)
