---
declaration: module
origin: cited
lean: ProbabilisticTheory.Representation.sector, ProbabilisticTheory.Representation.mem_sector, ProbabilisticTheory.Representation.cobound, ProbabilisticTheory.Representation.sub_smul_mem_cobound, ProbabilisticTheory.Representation.Fiber, ProbabilisticTheory.Representation.Fiber.mk, ProbabilisticTheory.Representation.Fiber.mk_action, ProbabilisticTheory.Representation.IsEquivariant
statement: formalized
proof: formalized
---

# Crystal momentum sectors

The module `PhyslibAlpha.ProbabilisticTheory.Representation.MomentumSectors`, [PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean): 22 declarations, 14 with a docstring.

> Sectors and fibers of definite crystal momentum for a translation-invariant system, and their
> conservation.

## i. Overview

> The translation symmetry of a crystal has a basic consequence: a time evolution, a
> Hamiltonian, or a response function that commutes with lattice translations conserves crystal
> momentum. Let translations `g` act linearly on a vector space `V`, the states or the observables of
> the crystal, by `β g`, and let `χ g` be the phase picked up by a translation: for a lattice
> translation `n` and wavevector `k`, `χ n = exp (i k n)`. Two spaces are attached to `χ`:
>
> * the *sector of momentum `χ`*, the vectors with `β g v = χ g v` for all `g`: the Bloch waves;
> * the *fiber at momentum `χ`*, `V` modulo the differences `β g v - χ g v`.
>
> In an infinite crystal a configuration of finite extent contains no Bloch wave, so the sector can
> be zero, whereas the fiber is the space of Fourier transforms evaluated at momentum `χ`. A linear
> map that commutes with the translations, such as the Hamiltonian, preserves every sector and acts
> on every fiber. Both statements are purely algebraic. No claim is made that the space decomposes
> into a sum of momentum sectors; that needs analysis and is a separate matter.

## ii. Key results

> - `sector` : the Bloch waves of crystal momentum `χ`.
> - `Fiber` : the space of crystal momentum `χ`, a quotient of the whole space.
> - `IsEquivariant` : a linear map commuting with the translations.
> - `IsEquivariant.mapsTo_sector` : a translation-invariant map conserves crystal momentum.
> - `IsEquivariant.fiberMap` : a translation-invariant map acts within each fiber.
> - `fiberMap_id`, `fiberMap_comp` : the action on fibers respects composition.
> - `sectorToFiber` : a Bloch wave defines a vector of the fiber of the same momentum.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapters 4 and 8.
> * F. Bloch, Über die Quantenmechanik der Elektronen in Kristallgittern, Z. Phys. 52 (1929). [ref:
>   bloch\_1929]

## A. Sectors and fibers

**`ProbabilisticTheory.Representation.sector`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L75).

> The momentum sector of the character `χ`: vectors on which `g` acts as the scalar `χ g`.

```lean
def sector (β : G →* Module.End K V) (χ : G → K) : Submodule K V
```

**`ProbabilisticTheory.Representation.mem_sector`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L81).

```lean
lemma mem_sector {β : G →* Module.End K V} {χ : G → K} {v : V} :
    v ∈ sector β χ ↔ ∀ g, β g v = χ g • v
```

**`ProbabilisticTheory.Representation.cobound`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L86).

> The submodule `span {β g v - χ g • v}` whose quotient is the momentum fiber. It is the
> "coboundary" submodule of the twisted action.

```lean
def cobound (β : G →* Module.End K V) (χ : G → K) : Submodule K V
```

**`ProbabilisticTheory.Representation.sub_smul_mem_cobound`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L89).

```lean
lemma sub_smul_mem_cobound (β : G →* Module.End K V) (χ : G → K) (g : G) (v : V) :
    β g v - χ g • v ∈ cobound β χ
```

**`ProbabilisticTheory.Representation.Fiber`**, an abbrev, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L94).

> The momentum fiber of the character `χ`: `V` modulo the vectors `β g v - χ g • v`.

```lean
abbrev Fiber (β : G →* Module.End K V) (χ : G → K) : Type _
```

**`ProbabilisticTheory.Representation.Fiber.mk`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L97).

> The canonical projection `V → V(χ)`.

```lean
def Fiber.mk (β : G →* Module.End K V) (χ : G → K) : V →ₗ[K] Fiber β χ
```

**`ProbabilisticTheory.Representation.Fiber.mk_action`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L101).

> In the fiber, `g` acts as the scalar `χ g`.

```lean
lemma Fiber.mk_action (β : G →* Module.End K V) (χ : G → K) (g : G) (v : V) :
    Fiber.mk β χ (β g v) = χ g • Fiber.mk β χ v
```

## B. Equivariant maps

**`ProbabilisticTheory.Representation.IsEquivariant`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L113).

> A linear map intertwining two actions of the same monoid.

```lean
def IsEquivariant (β : G →* Module.End K V) (β' : G →* Module.End K W)
    (T : V →ₗ[K] W) : Prop
```

**`ProbabilisticTheory.Representation.IsEquivariant.mapsTo_sector`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L121).

> Every equivariant linear map preserves each momentum sector.

```lean
lemma IsEquivariant.mapsTo_sector (hT : IsEquivariant β β' T) {v : V}
    (hv : v ∈ sector β χ) : T v ∈ sector β' χ
```

**`ProbabilisticTheory.Representation.IsEquivariant.sectorMap`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L126).

> The restriction of an equivariant map to a momentum sector.

```lean
def IsEquivariant.sectorMap (hT : IsEquivariant β β' T) (χ : G → K) :
    sector β χ →ₗ[K] sector β' χ
```

**`ProbabilisticTheory.Representation.IsEquivariant.coe_sectorMap`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L131).

```lean
lemma IsEquivariant.coe_sectorMap (hT : IsEquivariant β β' T) (v : sector β χ) :
    (hT.sectorMap χ v : W) = T v
```

**`ProbabilisticTheory.Representation.IsEquivariant.cobound_le_comap`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L136).

> An equivariant map sends the span defining the fiber of `V` into the span defining the fiber
> of `W`.

```lean
lemma IsEquivariant.cobound_le_comap (hT : IsEquivariant β β' T) (χ : G → K) :
    cobound β χ ≤ (cobound β' χ).comap T
```

**`ProbabilisticTheory.Representation.IsEquivariant.fiberMap`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L144).

> Every equivariant linear map induces a well-defined linear map on each momentum fiber.

```lean
def IsEquivariant.fiberMap (hT : IsEquivariant β β' T) (χ : G → K) :
    Fiber β χ →ₗ[K] Fiber β' χ
```

**`ProbabilisticTheory.Representation.IsEquivariant.fiberMap_mk`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L149).

```lean
lemma IsEquivariant.fiberMap_mk (hT : IsEquivariant β β' T) (χ : G → K) (v : V) :
    hT.fiberMap χ (Fiber.mk β χ v) = Fiber.mk β' χ (T v)
```

**`ProbabilisticTheory.Representation.IsEquivariant.fiberMap_comp_mk`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L153).

> The fiber map is the unique map making the square with the projections commute.

```lean
lemma IsEquivariant.fiberMap_comp_mk (hT : IsEquivariant β β' T) (χ : G → K) :
    (hT.fiberMap χ).comp (Fiber.mk β χ) = (Fiber.mk β' χ).comp T
```

## C. Functoriality

**`ProbabilisticTheory.Representation.isEquivariant_id`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L162).

```lean
lemma isEquivariant_id (β : G →* Module.End K V) : IsEquivariant β β LinearMap.id
```

**`ProbabilisticTheory.Representation.IsEquivariant.comp`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L165).

```lean
lemma IsEquivariant.comp (hS : IsEquivariant β' β'' S) (hT : IsEquivariant β β' T) :
    IsEquivariant β β'' (S ∘ₗ T)
```

**`ProbabilisticTheory.Representation.fiberMap_id`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L169).

```lean
lemma fiberMap_id (χ : G → K) :
    (isEquivariant_id β).fiberMap χ = LinearMap.id
```

**`ProbabilisticTheory.Representation.IsEquivariant.fiberMap_comp`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L173).

```lean
lemma IsEquivariant.fiberMap_comp (hS : IsEquivariant β' β'' S) (hT : IsEquivariant β β' T)
    (χ : G → K) :
    (hS.comp hT).fiberMap χ = (hS.fiberMap χ) ∘ₗ (hT.fiberMap χ)
```

**`ProbabilisticTheory.Representation.IsEquivariant.mapsTo_sector_self`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L181).

> Equivariant maps commute with the dynamics they generate: if `D` is an equivariant
> endomorphism, it preserves every sector and descends to every fiber. This is the form used for
> translation-invariant evolution.

```lean
lemma IsEquivariant.mapsTo_sector_self {D : V →ₗ[K] V} (hD : IsEquivariant β β D) {v : V}
    (hv : v ∈ sector β χ) : D v ∈ sector β χ
```

## D. From sectors to fibers

**`ProbabilisticTheory.Representation.sectorToFiber`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L191).

> The canonical map from the sector of `χ` to the fiber of `χ`.

```lean
def sectorToFiber (β : G →* Module.End K V) (χ : G → K) :
    sector β χ →ₗ[K] Fiber β χ
```

**`ProbabilisticTheory.Representation.IsEquivariant.fiberMap_comp_sectorToFiber`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean#L196).

> The canonical map from sector to fiber is natural for equivariant maps.

```lean
lemma IsEquivariant.fiberMap_comp_sectorToFiber (hT : IsEquivariant β β' T) (χ : G → K) :
    (hT.fiberMap χ).comp (sectorToFiber β χ)
      = (sectorToFiber β' χ).comp (hT.sectorMap χ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/MomentumSectors.lean)
