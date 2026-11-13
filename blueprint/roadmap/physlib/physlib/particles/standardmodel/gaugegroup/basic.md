---
declaration: module
origin: cited
lean: StandardModel.GaugeGroupI, StandardModel.GaugeGroupI.toSU3, StandardModel.GaugeGroupI.toSU2, StandardModel.GaugeGroupI.toU1, StandardModel.GaugeGroupI.ext, StandardModel.GaugeGroupI.star_eq, StandardModel.GaugeGroupI.star_toSU3, StandardModel.GaugeGroupI.star_toSU2
statement: formalized
proof: formalized
---

# The Standard Model Gauge Group

The module `Physlib.Particles.StandardModel.GaugeGroup.Basic`, [Physlib/Particles/StandardModel/GaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean): 102 declarations (6 instances with no name), 35 with a docstring.

> The standard model gauge group, `SU(3) x SU(2) x U(1)` and its quotients.

## References

> * Baez's Grand Unified Theories notes, cited throughout below. [ref: baez\_guts\_notes]

## The unquotiented gauge group

**`StandardModel.GaugeGroupI`**, an abbrev, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L39).

> The global gauge group of the Standard Model with no discrete quotients.
> The `I` in the Name is an indication of the statement that this has no discrete quotients.

```lean
abbrev GaugeGroupI : Type
```

**`StandardModel.GaugeGroupI.toSU3`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L45).

> The underlying element of `SU(3)` of an element in `GaugeGroupI`.

```lean
def toSU3 : GaugeGroupI →* specialUnitaryGroup (Fin 3) ℂ
```

**`StandardModel.GaugeGroupI.toSU2`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L51).

> The underlying element of `SU(2)` of an element in `GaugeGroupI`.

```lean
def toSU2 : GaugeGroupI →* specialUnitaryGroup (Fin 2) ℂ
```

**`StandardModel.GaugeGroupI.toU1`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L57).

> The underlying element of `U(1)` of an element in `GaugeGroupI`.

```lean
def toU1 : GaugeGroupI →* unitary ℂ
```

**`StandardModel.GaugeGroupI.ext`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L63).

```lean
lemma ext {g g' : GaugeGroupI} (hSU3 : toSU3 g = toSU3 g')
    (hSU2 : toSU2 g = toSU2 g') (hU1 : toU1 g = toU1 g') : g = g'
```

**An instance with no name**, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L67).

```lean
instance : Star GaugeGroupI
```

**`StandardModel.GaugeGroupI.star_eq`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L70).

```lean
lemma star_eq (g : GaugeGroupI) : star g = (star g.1, star g.2.1, star g.2.2)
```

**`StandardModel.GaugeGroupI.star_toSU3`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L73).

```lean
lemma star_toSU3 (g : GaugeGroupI) : toSU3 (star g) = star (toSU3 g)
```

**`StandardModel.GaugeGroupI.star_toSU2`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L76).

```lean
lemma star_toSU2 (g : GaugeGroupI) : toSU2 (star g) = star (toSU2 g)
```

**`StandardModel.GaugeGroupI.star_toU1`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L79).

```lean
lemma star_toU1 (g : GaugeGroupI) : toU1 (star g) = star (toU1 g)
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L81).

```lean
instance : InvolutiveStar GaugeGroupI
```

**`StandardModel.GaugeGroupI.diagSU2`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L87).

> The diagonal element `diag(a, ā)` of `SU(2)` associated with a phase `a`.
> These elements form a maximal torus of `SU(2)`.

```lean
noncomputable def diagSU2 : unitary ℂ →* specialUnitaryGroup (Fin 2) ℂ
```

**`StandardModel.GaugeGroupI.diagSU2_coe`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L103).

```lean
lemma diagSU2_coe (a : unitary ℂ) :
    (diagSU2 a : Matrix (Fin 2) (Fin 2) ℂ) = !![(a : ℂ), 0; 0, (star a : ℂ)]
```

**`StandardModel.GaugeGroupI.eq_diagSU2_of_apply_zero_one_eq_zero`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L108).

> An element of `SU(2)` whose upper-right entry vanishes and whose lower-right entry is `w̄`,
> for a phase `w`, is the diagonal element `diag(w, w̄)`.

```lean
lemma eq_diagSU2_of_apply_zero_one_eq_zero {M : specialUnitaryGroup (Fin 2) ℂ} {w : unitary ℂ}
    (h01 : (M : Matrix (Fin 2) (Fin 2) ℂ) 0 1 = 0)
    (h11 : (M : Matrix (Fin 2) (Fin 2) ℂ) 1 1 = conj (w : ℂ)) : M = diagSU2 w
```

**`StandardModel.GaugeGroupI.electromagnetismU1`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L131).

> The electromagnetic `U(1)`: the embedding of `U(1)` into the gauge group given by
> `u ↦ (1, diag(u³, ū³), u)`, trivial on `SU(3)`. It is generated by the electric charge
> `Q = T₃ + Y`, in the normalisation `6Q = 6T₃ + 6Y` where the hypercharges `6Y` are integers.
> It is the subgroup left unbroken by a Higgs vacuum of the form `(0, v)`.

```lean
noncomputable def electromagnetismU1 : unitary ℂ →* GaugeGroupI
```

**`StandardModel.GaugeGroupI.electromagnetismU1_toSU3`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L138).

```lean
lemma electromagnetismU1_toSU3 (u1 : unitary ℂ) :
    toSU3 (electromagnetismU1 u1) = 1
```

**`StandardModel.GaugeGroupI.electromagnetismU1_toSU2`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L142).

```lean
lemma electromagnetismU1_toSU2 (u1 : unitary ℂ) :
    toSU2 (electromagnetismU1 u1) = diagSU2 (u1 ^ 3)
```

**`StandardModel.GaugeGroupI.electromagnetismU1_toU1`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L146).

```lean
lemma electromagnetismU1_toU1 (u1 : unitary ℂ) :
    toU1 (electromagnetismU1 u1) = u1
```

**`StandardModel.GaugeGroupI.electromagnetismU1_injective`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L149).

```lean
lemma electromagnetismU1_injective : Function.Injective electromagnetismU1
```

## The ℤ₆ quotient

**`StandardModel.gaugeGroupℤ₆UnitaryOfRoot`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L161).

> The unitary complex number associated to a sixth root of unity.

```lean
noncomputable def gaugeGroupℤ₆UnitaryOfRoot (α : rootsOfUnity 6 ℂ) : unitary ℂ
```

**`StandardModel.gaugeGroupℤ₆UnitaryOfRoot_coe`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L171).

```lean
lemma gaugeGroupℤ₆UnitaryOfRoot_coe (α : rootsOfUnity 6 ℂ) :
    (gaugeGroupℤ₆UnitaryOfRoot α : ℂ) = ((α : ℂˣ) : ℂ)
```

**`StandardModel.gaugeGroupℤ₆SU3OfRoot`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L175).

> The `SU(3)` scalar matrix associated to a sixth root of unity.

```lean
noncomputable def gaugeGroupℤ₆SU3OfRoot (α : rootsOfUnity 6 ℂ) :
    specialUnitaryGroup (Fin 3) ℂ
```

**`StandardModel.gaugeGroupℤ₆SU3OfRoot_eq_mul_id`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L198).

```lean
lemma gaugeGroupℤ₆SU3OfRoot_eq_mul_id (α : rootsOfUnity 6 ℂ) :
    (gaugeGroupℤ₆SU3OfRoot α).1 = ((α : ℂˣ) : ℂ) ^ 2 • 1
```

**`StandardModel.gaugeGroupℤ₆SU3OfRoot_toEuclideanLin_apply`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L203).

```lean
lemma gaugeGroupℤ₆SU3OfRoot_toEuclideanLin_apply (α : rootsOfUnity 6 ℂ)
    (v : EuclideanSpace ℂ (Fin 3)) :
    (gaugeGroupℤ₆SU3OfRoot α).1.toEuclideanLin v = ((α : ℂˣ) : ℂ) ^ 2 • v
```

**`StandardModel.gaugeGroupℤ₆SU2OfRoot`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L209).

> The `SU(2)` scalar matrix associated to a sixth root of unity.

```lean
noncomputable def gaugeGroupℤ₆SU2OfRoot (α : rootsOfUnity 6 ℂ) :
    specialUnitaryGroup (Fin 2) ℂ
```

**`StandardModel.gaugeGroupℤ₆SU2OfRoot_eq_mul_id`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L238).

```lean
lemma gaugeGroupℤ₆SU2OfRoot_eq_mul_id (α : rootsOfUnity 6 ℂ) :
    (gaugeGroupℤ₆SU2OfRoot α).1 = star ((α : ℂˣ) : ℂ) ^ 3 • 1
```

**`StandardModel.gaugeGroupℤ₆SU2OfRoot_toEuclideanLin_apply`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L243).

```lean
lemma gaugeGroupℤ₆SU2OfRoot_toEuclideanLin_apply (α : rootsOfUnity 6 ℂ)
    (v : EuclideanSpace ℂ (Fin 2)) :
    (gaugeGroupℤ₆SU2OfRoot α).1.toEuclideanLin v = star ((α : ℂˣ) : ℂ) ^ 3 • v
```

**`StandardModel.gaugeGroupℤ₆OfRoot`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L249).

> The element of `GaugeGroupI` associated to a sixth root of unity.

```lean
noncomputable def gaugeGroupℤ₆OfRoot (α : rootsOfUnity 6 ℂ) : GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₆OfRoot_toSU3`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L253).

```lean
lemma gaugeGroupℤ₆OfRoot_toSU3 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₆OfRoot α) = gaugeGroupℤ₆SU3OfRoot α
```

**`StandardModel.gaugeGroupℤ₆OfRoot_toSU2`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L257).

```lean
lemma gaugeGroupℤ₆OfRoot_toSU2 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₆OfRoot α) = gaugeGroupℤ₆SU2OfRoot α
```

**`StandardModel.gaugeGroupℤ₆OfRoot_toU1`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L261).

```lean
lemma gaugeGroupℤ₆OfRoot_toU1 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₆OfRoot α) = gaugeGroupℤ₆UnitaryOfRoot α
```

**`StandardModel.gaugeGroupℤ₆OfRoot_mem_center`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L264).

```lean
lemma gaugeGroupℤ₆OfRoot_mem_center (α : rootsOfUnity 6 ℂ) :
    gaugeGroupℤ₆OfRoot α ∈ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₆Hom`**, a def, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L272).

> The homomorphism from sixth roots of unity to `GaugeGroupI`.

```lean
noncomputable def gaugeGroupℤ₆Hom : rootsOfUnity 6 ℂ →* GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₆Hom_apply`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L304).

```lean
lemma gaugeGroupℤ₆Hom_apply (α : rootsOfUnity 6 ℂ) :
    gaugeGroupℤ₆Hom α = gaugeGroupℤ₆OfRoot α
```

**`StandardModel.gaugeGroupℤ₆Hom_toSU3`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L308).

```lean
lemma gaugeGroupℤ₆Hom_toSU3 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₆Hom α) = gaugeGroupℤ₆SU3OfRoot α
```

**`StandardModel.gaugeGroupℤ₆Hom_toSU2`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L312).

```lean
lemma gaugeGroupℤ₆Hom_toSU2 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₆Hom α) = gaugeGroupℤ₆SU2OfRoot α
```

**`StandardModel.gaugeGroupℤ₆Hom_toU1`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L316).

```lean
lemma gaugeGroupℤ₆Hom_toU1 (α : rootsOfUnity 6 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₆Hom α) = gaugeGroupℤ₆UnitaryOfRoot α
```

**`StandardModel.gaugeGroupℤ₆SubGroup`**, a def, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L325).

> The subgroup of the un-quotiented gauge group which acts trivially on all particles in the
> standard model, i.e., the ℤ₆-subgroup of `GaugeGroupI` with elements `(α^2 * I₃, α^(-3) * I₂, α)`,
> where `α` is a sixth complex root of unity.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
noncomputable def gaugeGroupℤ₆SubGroup : Subgroup GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₆OfRoot_mem`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L328).

```lean
lemma gaugeGroupℤ₆OfRoot_mem (α : rootsOfUnity 6 ℂ) :
    gaugeGroupℤ₆OfRoot α ∈ gaugeGroupℤ₆SubGroup
```

**`StandardModel.mem_gaugeGroupℤ₆SubGroup_iff`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L332).

```lean
lemma mem_gaugeGroupℤ₆SubGroup_iff (g : GaugeGroupI) :
    g ∈ gaugeGroupℤ₆SubGroup ↔ ∃ α : rootsOfUnity 6 ℂ, gaugeGroupℤ₆OfRoot α = g
```

**`StandardModel.gaugeGroupℤ₆SubGroup_le_center`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L336).

```lean
lemma gaugeGroupℤ₆SubGroup_le_center :
    gaugeGroupℤ₆SubGroup ≤ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₆SubGroup_normal`**, an instance, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L341).

```lean
instance gaugeGroupℤ₆SubGroup_normal : gaugeGroupℤ₆SubGroup.Normal
```

**`StandardModel.GaugeGroupℤ₆`**, a def, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L351).

> The smallest possible gauge group of the Standard Model, i.e., the quotient of `GaugeGroupI` by
> the ℤ₆-subgroup `gaugeGroupℤ₆SubGroup`.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
def GaugeGroupℤ₆ : Type
```

**An instance with no name**, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L354).

```lean
noncomputable instance : Group GaugeGroupℤ₆
```

**`StandardModel.GaugeGroupℤ₆.mk`**, a def, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L360).

> The quotient map from `GaugeGroupI` to `GaugeGroupℤ₆`.

```lean
noncomputable def mk : GaugeGroupI →* GaugeGroupℤ₆
```

**`StandardModel.GaugeGroupℤ₆.mk_gaugeGroupℤ₆OfRoot`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L364).

```lean
lemma mk_gaugeGroupℤ₆OfRoot (α : rootsOfUnity 6 ℂ) :
    mk (gaugeGroupℤ₆OfRoot α) = 1
```

## The ℤ₂ quotient

**`StandardModel.gaugeGroupℤ₂RootToℤ₆Root`**, a def, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L377).

> The inclusion of second roots of unity into sixth roots of unity.

```lean
noncomputable def gaugeGroupℤ₂RootToℤ₆Root : rootsOfUnity 2 ℂ →* rootsOfUnity 6 ℂ
```

**`StandardModel.gaugeGroupℤ₂OfRoot`**, a def, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L381).

> The element of `GaugeGroupI` associated to a second root of unity.

```lean
noncomputable def gaugeGroupℤ₂OfRoot (α : rootsOfUnity 2 ℂ) : GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₂OfRoot_toSU3`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L385).

```lean
lemma gaugeGroupℤ₂OfRoot_toSU3 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₂OfRoot α) =
      gaugeGroupℤ₆SU3OfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂OfRoot_toSU2`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L390).

```lean
lemma gaugeGroupℤ₂OfRoot_toSU2 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₂OfRoot α) =
      gaugeGroupℤ₆SU2OfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂OfRoot_toU1`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L395).

```lean
lemma gaugeGroupℤ₂OfRoot_toU1 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₂OfRoot α) =
      gaugeGroupℤ₆UnitaryOfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂OfRoot_mem_center`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L399).

```lean
lemma gaugeGroupℤ₂OfRoot_mem_center (α : rootsOfUnity 2 ℂ) :
    gaugeGroupℤ₂OfRoot α ∈ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₂Hom`**, a def, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L404).

> The homomorphism from second roots of unity to `GaugeGroupI`.

```lean
noncomputable def gaugeGroupℤ₂Hom : rootsOfUnity 2 ℂ →* GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₂Hom_apply`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L408).

```lean
lemma gaugeGroupℤ₂Hom_apply (α : rootsOfUnity 2 ℂ) :
    gaugeGroupℤ₂Hom α = gaugeGroupℤ₂OfRoot α
```

**`StandardModel.gaugeGroupℤ₂Hom_toSU3`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L412).

```lean
lemma gaugeGroupℤ₂Hom_toSU3 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₂Hom α) =
      gaugeGroupℤ₆SU3OfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂Hom_toSU2`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L417).

```lean
lemma gaugeGroupℤ₂Hom_toSU2 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₂Hom α) =
      gaugeGroupℤ₆SU2OfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂Hom_toU1`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L422).

```lean
lemma gaugeGroupℤ₂Hom_toU1 (α : rootsOfUnity 2 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₂Hom α) =
      gaugeGroupℤ₆UnitaryOfRoot (gaugeGroupℤ₂RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₂SubGroup`**, a def, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L432).

> The ℤ₂-subgroup of the un-quotiented gauge group which acts trivially on all particles in the
> standard model, i.e., the ℤ₂-subgroup of `GaugeGroupI` derived from the ℤ₂ subgroup of
> `gaugeGroupℤ₆SubGroup`.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
noncomputable def gaugeGroupℤ₂SubGroup : Subgroup GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₂OfRoot_mem`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L435).

```lean
lemma gaugeGroupℤ₂OfRoot_mem (α : rootsOfUnity 2 ℂ) :
    gaugeGroupℤ₂OfRoot α ∈ gaugeGroupℤ₂SubGroup
```

**`StandardModel.mem_gaugeGroupℤ₂SubGroup_iff`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L439).

```lean
lemma mem_gaugeGroupℤ₂SubGroup_iff (g : GaugeGroupI) :
    g ∈ gaugeGroupℤ₂SubGroup ↔ ∃ α : rootsOfUnity 2 ℂ, gaugeGroupℤ₂OfRoot α = g
```

**`StandardModel.gaugeGroupℤ₂SubGroup_le_gaugeGroupℤ₆SubGroup`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L443).

```lean
lemma gaugeGroupℤ₂SubGroup_le_gaugeGroupℤ₆SubGroup :
    gaugeGroupℤ₂SubGroup ≤ gaugeGroupℤ₆SubGroup
```

**`StandardModel.gaugeGroupℤ₂SubGroup_le_center`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L448).

```lean
lemma gaugeGroupℤ₂SubGroup_le_center :
    gaugeGroupℤ₂SubGroup ≤ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₂SubGroup_normal`**, an instance, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L452).

```lean
instance gaugeGroupℤ₂SubGroup_normal : gaugeGroupℤ₂SubGroup.Normal
```

**`StandardModel.GaugeGroupℤ₂`**, a def, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L462).

> The gauge group of the Standard Model with a ℤ₂ quotient, i.e., the quotient of `GaugeGroupI` by
> the ℤ₂-subgroup `gaugeGroupℤ₂SubGroup`.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
def GaugeGroupℤ₂ : Type
```

**An instance with no name**, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L465).

```lean
noncomputable instance : Group GaugeGroupℤ₂
```

**`StandardModel.GaugeGroupℤ₂.mk`**, a def, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L471).

> The quotient map from `GaugeGroupI` to `GaugeGroupℤ₂`.

```lean
noncomputable def mk : GaugeGroupI →* GaugeGroupℤ₂
```

**`StandardModel.GaugeGroupℤ₂.mk_gaugeGroupℤ₂OfRoot`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L475).

```lean
lemma mk_gaugeGroupℤ₂OfRoot (α : rootsOfUnity 2 ℂ) :
    mk (gaugeGroupℤ₂OfRoot α) = 1
```

## The ℤ₃ quotient

**`StandardModel.gaugeGroupℤ₃RootToℤ₆Root`**, a def, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L488).

> The inclusion of third roots of unity into sixth roots of unity.

```lean
noncomputable def gaugeGroupℤ₃RootToℤ₆Root : rootsOfUnity 3 ℂ →* rootsOfUnity 6 ℂ
```

**`StandardModel.gaugeGroupℤ₃OfRoot`**, a def, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L492).

> The element of `GaugeGroupI` associated to a third root of unity.

```lean
noncomputable def gaugeGroupℤ₃OfRoot (α : rootsOfUnity 3 ℂ) : GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₃OfRoot_toSU3`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L496).

```lean
lemma gaugeGroupℤ₃OfRoot_toSU3 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₃OfRoot α) =
      gaugeGroupℤ₆SU3OfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃OfRoot_toSU2`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L501).

```lean
lemma gaugeGroupℤ₃OfRoot_toSU2 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₃OfRoot α) =
      gaugeGroupℤ₆SU2OfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃OfRoot_toU1`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L506).

```lean
lemma gaugeGroupℤ₃OfRoot_toU1 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₃OfRoot α) =
      gaugeGroupℤ₆UnitaryOfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃OfRoot_mem_center`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L510).

```lean
lemma gaugeGroupℤ₃OfRoot_mem_center (α : rootsOfUnity 3 ℂ) :
    gaugeGroupℤ₃OfRoot α ∈ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₃Hom`**, a def, [line 515](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L515).

> The homomorphism from third roots of unity to `GaugeGroupI`.

```lean
noncomputable def gaugeGroupℤ₃Hom : rootsOfUnity 3 ℂ →* GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₃Hom_apply`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L519).

```lean
lemma gaugeGroupℤ₃Hom_apply (α : rootsOfUnity 3 ℂ) :
    gaugeGroupℤ₃Hom α = gaugeGroupℤ₃OfRoot α
```

**`StandardModel.gaugeGroupℤ₃Hom_toSU3`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L523).

```lean
lemma gaugeGroupℤ₃Hom_toSU3 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toSU3 (gaugeGroupℤ₃Hom α) =
      gaugeGroupℤ₆SU3OfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃Hom_toSU2`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L528).

```lean
lemma gaugeGroupℤ₃Hom_toSU2 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toSU2 (gaugeGroupℤ₃Hom α) =
      gaugeGroupℤ₆SU2OfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃Hom_toU1`**, a lemma, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L533).

```lean
lemma gaugeGroupℤ₃Hom_toU1 (α : rootsOfUnity 3 ℂ) :
    GaugeGroupI.toU1 (gaugeGroupℤ₃Hom α) =
      gaugeGroupℤ₆UnitaryOfRoot (gaugeGroupℤ₃RootToℤ₆Root α)
```

**`StandardModel.gaugeGroupℤ₃SubGroup`**, a def, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L543).

> The ℤ₃-subgroup of the un-quotiented gauge group which acts trivially on all particles in the
> standard model, i.e., the ℤ₃-subgroup of `GaugeGroupI` derived from the ℤ₃ subgroup of
> `gaugeGroupℤ₆SubGroup`.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
noncomputable def gaugeGroupℤ₃SubGroup : Subgroup GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₃OfRoot_mem`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L546).

```lean
lemma gaugeGroupℤ₃OfRoot_mem (α : rootsOfUnity 3 ℂ) :
    gaugeGroupℤ₃OfRoot α ∈ gaugeGroupℤ₃SubGroup
```

**`StandardModel.mem_gaugeGroupℤ₃SubGroup_iff`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L550).

```lean
lemma mem_gaugeGroupℤ₃SubGroup_iff (g : GaugeGroupI) :
    g ∈ gaugeGroupℤ₃SubGroup ↔ ∃ α : rootsOfUnity 3 ℂ, gaugeGroupℤ₃OfRoot α = g
```

**`StandardModel.gaugeGroupℤ₃SubGroup_le_gaugeGroupℤ₆SubGroup`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L554).

```lean
lemma gaugeGroupℤ₃SubGroup_le_gaugeGroupℤ₆SubGroup :
    gaugeGroupℤ₃SubGroup ≤ gaugeGroupℤ₆SubGroup
```

**`StandardModel.gaugeGroupℤ₃SubGroup_le_center`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L559).

```lean
lemma gaugeGroupℤ₃SubGroup_le_center :
    gaugeGroupℤ₃SubGroup ≤ Subgroup.center GaugeGroupI
```

**`StandardModel.gaugeGroupℤ₃SubGroup_normal`**, an instance, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L563).

```lean
instance gaugeGroupℤ₃SubGroup_normal : gaugeGroupℤ₃SubGroup.Normal
```

**`StandardModel.GaugeGroupℤ₃`**, a def, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L573).

> The gauge group of the Standard Model with a ℤ₃-quotient, i.e., the quotient of `GaugeGroupI` by
> the ℤ₃-subgroup `gaugeGroupℤ₃SubGroup`.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
def GaugeGroupℤ₃ : Type
```

**An instance with no name**, [line 576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L576).

```lean
noncomputable instance : Group GaugeGroupℤ₃
```

**`StandardModel.GaugeGroupℤ₃.mk`**, a def, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L582).

> The quotient map from `GaugeGroupI` to `GaugeGroupℤ₃`.

```lean
noncomputable def mk : GaugeGroupI →* GaugeGroupℤ₃
```

**`StandardModel.GaugeGroupℤ₃.mk_gaugeGroupℤ₃OfRoot`**, a lemma, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L586).

```lean
lemma mk_gaugeGroupℤ₃OfRoot (α : rootsOfUnity 3 ℂ) :
    mk (gaugeGroupℤ₃OfRoot α) = 1
```

## Gauge groups from quotient choices

**`StandardModel.GaugeGroupQuot`**, an inductive, [line 601](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L601).

> Specifies the allowed quotients of `SU(3) x SU(2) x U(1)` which give a valid
> gauge group of the Standard Model.

```lean
inductive GaugeGroupQuot : Type
  /-- The element of `GaugeGroupQuot` corresponding to the quotient of the full SM gauge group
    by the sub-group `ℤ₆`. -/
  | ℤ₆ : GaugeGroupQuot
  /-- The element of `GaugeGroupQuot` corresponding to the quotient of the full SM gauge group
    by the sub-group `ℤ₂`. -/
  | ℤ₂ : GaugeGroupQuot
  /-- The element of `GaugeGroupQuot` corresponding to the quotient of the full SM gauge group
    by the sub-group `ℤ₃`. -/
  | ℤ₃ : GaugeGroupQuot
  /-- The element of `GaugeGroupQuot` corresponding to the full SM gauge group. -/
  | I : GaugeGroupQuot
```

**`StandardModel.GaugeGroup`**, a def, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L621).

> The (global) gauge group of the Standard Model given a choice of quotient, i.e., the map from
> `GaugeGroupQuot` to `Type` which gives the gauge group of the Standard Model for a given choice of
> quotient.
>
> See https://math.ucr.edu/home/baez/guts.pdf [ref: baez\_guts\_notes]

```lean
def GaugeGroup : GaugeGroupQuot → Type
```

**An instance with no name**, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L627).

```lean
noncomputable instance (q : GaugeGroupQuot) : Group (GaugeGroup q)
```

**`StandardModel.GaugeGroupQuot.subgroup`**, a def, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L633).

> The central subgroup of `GaugeGroupI` quotiented by a gauge-group quotient choice.

```lean
noncomputable def subgroup : GaugeGroupQuot → Subgroup GaugeGroupI
```

**`StandardModel.GaugeGroupQuot.subgroup_le_center`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L640).

> The subgroup attached to a gauge-group quotient choice lies in the center of `GaugeGroupI`.

```lean
lemma subgroup_le_center (q : GaugeGroupQuot) :
    subgroup q ≤ Subgroup.center GaugeGroupI
```

**`StandardModel.GaugeGroupQuot.subgroup_normal`**, an instance, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L649).

> The subgroup attached to a gauge-group quotient choice is normal in `GaugeGroupI`.

```lean
instance subgroup_normal (q : GaugeGroupQuot) : (subgroup q).Normal
```

**`StandardModel.GaugeGroupQuot.subgroup_le_subgroup_ℤ₆`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L656).

```lean
lemma subgroup_le_subgroup_ℤ₆ (q : GaugeGroupQuot) : subgroup q ≤ gaugeGroupℤ₆SubGroup
```

**`StandardModel.GaugeGroupQuot.quotientMap`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L667).

> The quotient map from `GaugeGroupI` to the gauge group selected by a quotient choice.

```lean
noncomputable def quotientMap (q : GaugeGroupQuot) : GaugeGroupI →* GaugeGroup q
```

**`StandardModel.GaugeGroupQuot.quotientMap_I_apply`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L675).

```lean
lemma quotientMap_I_apply (g : GaugeGroupI) :
    quotientMap .I g = g
```

**`StandardModel.GaugeGroupQuot.quotientMap_ℤ₆_gaugeGroupℤ₆OfRoot`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L679).

```lean
lemma quotientMap_ℤ₆_gaugeGroupℤ₆OfRoot (α : rootsOfUnity 6 ℂ) :
    quotientMap .ℤ₆ (gaugeGroupℤ₆OfRoot α) = 1
```

**`StandardModel.GaugeGroupQuot.quotientMap_ℤ₂_gaugeGroupℤ₂OfRoot`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L684).

```lean
lemma quotientMap_ℤ₂_gaugeGroupℤ₂OfRoot (α : rootsOfUnity 2 ℂ) :
    quotientMap .ℤ₂ (gaugeGroupℤ₂OfRoot α) = 1
```

**`StandardModel.GaugeGroupQuot.quotientMap_ℤ₃_gaugeGroupℤ₃OfRoot`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L689).

```lean
lemma quotientMap_ℤ₃_gaugeGroupℤ₃OfRoot (α : rootsOfUnity 3 ℂ) :
    quotientMap .ℤ₃ (gaugeGroupℤ₃OfRoot α) = 1
```

**`StandardModel.GaugeGroupQuot.mem_subgroup_iff_quotientMap_eq_one`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L694).

> The kernel of the quotient map is the subgroup selected by the quotient choice.

```lean
lemma mem_subgroup_iff_quotientMap_eq_one (q : GaugeGroupQuot) (g : GaugeGroupI) :
    g ∈ subgroup q ↔ quotientMap q g = 1
```

**`StandardModel.GaugeGroupQuot.quotientMap_eq_iff`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean#L702).

> Two representatives have the same image under the selected quotient map exactly when their
> quotient lies in the subgroup selected by the quotient choice.

```lean
lemma quotientMap_eq_iff (q : GaugeGroupQuot) (g h : GaugeGroupI) :
    quotientMap q g = quotientMap q h ↔ g / h ∈ subgroup q
```

## Smoothness structure on the gauge group.

## Gauge bundles and transformations

## Depends on

- [Physlib.Meta.Informal.Basic](../../../meta/informal/basic.md)

## Sources

- [Physlib/Particles/StandardModel/GaugeGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/GaugeGroup/Basic.lean)
