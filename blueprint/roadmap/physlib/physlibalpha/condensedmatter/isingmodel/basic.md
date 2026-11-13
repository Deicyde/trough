---
declaration: module
origin: cited
lean: CondensedMatter.IsingModel, CondensedMatter.IsingModel.Configuration, CondensedMatter.IsingModel.spin, CondensedMatter.IsingModel.abs_spin, CondensedMatter.IsingModel.pairSpin, CondensedMatter.IsingModel.energy, CondensedMatter.IsingModel.energy_congr, CondensedMatter.IsingModel.pairSpin_comm
statement: formalized
proof: formalized
---

# Classical Ising interactions on a graph

The module `PhyslibAlpha.CondensedMatter.IsingModel.Basic`, [PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean): 30 declarations, 30 with a docstring.

## i. Overview

> A classical Ising configuration assigns an up or down spin to every vertex of a graph.
> Edges specify which spins interact. `IsingModel` adds a uniform exchange coupling `J`
> and longitudinal field `h`, both in a fixed energy unit, to this connectivity.
>
> The energy of a finite region is
> `-J ∑ {x,y} σ(x) σ(y) - h ∑ x σ(x)`, where the first sum runs over its internal graph edges
> and each spin has value ±1. We implement the edge sum as half the sum over ordered adjacent pairs:
> symmetry counts each undirected edge twice and the simple graph excludes self-interactions.
> Positive `J` favors alignment (ferromagnetism), negative `J` favors opposite spins,
> and positive `h` favors up spins.
>
> Joining disjoint regions changes their combined energy only through bonds connecting the
> regions. Each crossing bond contributes at most `|J|` in absolute value. If sites have at
> most `q` neighbors, the absolute energy is bounded by `(|J| q / 2 + |h|) |Λ|`. These bounds
> control boundary corrections and energy growth with volume.
>
> For ferromagnetic exchange `J ≥ 0`, uniform polarization aligned with the field attains
> the least energy on every finite region. Its energy per site converges whenever the
> average internal coordination converges. These results apply to arbitrary graphs;
> crystal translations supply an additional symmetry.

## ii. Key results

> - `IsingModel` : the nearest-neighbour Ising model on a graph, with uniform coupling and field.
> - `IsingModel.energy` : the energy of a finite region.
> - `IsingModel.abs_energy_union_sub_le` : the failure of additivity is bounded by the crossing bonds.
> - `IsingModel.abs_energy_le_of_degree_le` : the energy grows at most linearly with the volume.
> - `IsingModel.groundEnergy_eq` : the ferromagnetic ground-state energy of a region.
> - `IsingModel.tendsto_groundEnergyDensity` : the ground-state energy density converges when the
>   average internal coordination does.
> - `IsingModel.energy_translate` : the energy is invariant under crystal translations.

## iv. References

> * E. Ising, Beitrag zur Theorie des Ferromagnetismus.

**`CondensedMatter.IsingModel`**, a structure, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L70).

> A classical nearest-neighbor Ising model on the specified undirected graph.

```lean
structure IsingModel {X : Type*} (graph : SimpleGraph X) where
  /-- Uniform exchange coupling; positive values favor aligned spins. -/
  J : ℝ
  /-- Uniform longitudinal field; positive values favor up spins. -/
  h : ℝ
```

## A. Spin configurations

**`CondensedMatter.IsingModel.Configuration`**, an abbrev, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L85).

> Up or down spins at every site of the crystal.

```lean
abbrev Configuration (_I : IsingModel g)
```

**`CondensedMatter.IsingModel.spin`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L88).

> The dimensionless spin value, with `true` denoting up.

```lean
def spin (b : Bool) : ℝ
```

**`CondensedMatter.IsingModel.abs_spin`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L91).

> Every Ising spin has unit magnitude.

```lean
lemma abs_spin (b : Bool) : |spin b| = 1
```

## B. Finite-region energy and locality

**`CondensedMatter.IsingModel.pairSpin`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L97).

> The exchange contribution of an ordered pair; nonadjacent sites contribute zero.

```lean
noncomputable def pairSpin (I : IsingModel g) (σ : I.Configuration) (x y : X) : ℝ
```

**`CondensedMatter.IsingModel.energy`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L102).

> Energy of the spins and internal edges of a finite region. The factor `1/2` counts each
> undirected graph edge once. Spins outside the region do not contribute.

```lean
noncomputable def energy (I : IsingModel g) (Λ : Finset X)
    (σ : I.Configuration) : ℝ
```

**`CondensedMatter.IsingModel.energy_congr`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L107).

> A region's energy depends only on the spin configuration inside that region.

```lean
lemma energy_congr (I : IsingModel g) (Λ : Finset X) {σ τ : I.Configuration}
    (hστ : ∀ x ∈ Λ, σ x = τ x) : I.energy Λ σ = I.energy Λ τ
```

## C. Boundary interactions

> Combining disjoint regions adds precisely the exchange interactions across their common
> boundary. The number of crossing bonds bounds this correction independently of the spin
> configuration.

**`CondensedMatter.IsingModel.pairSpin_comm`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L128).

> The exchange contribution is symmetric in the endpoints of a bond.

```lean
lemma pairSpin_comm (I : IsingModel g) (σ : I.Configuration) (x y : X) :
    I.pairSpin σ x y = I.pairSpin σ y x
```

**`CondensedMatter.IsingModel.energy_union`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L133).

> Joining disjoint regions adds exactly their crossing exchange interactions.

```lean
lemma energy_union [DecidableEq X] (I : IsingModel g) (Λ M : Finset X)
    (hΛM : Disjoint Λ M) (σ : I.Configuration) :
    I.energy (Λ ∪ M) σ = I.energy Λ σ + I.energy M σ -
      I.J * ∑ x ∈ Λ, ∑ y ∈ M, I.pairSpin σ x y
```

**`CondensedMatter.IsingModel.abs_pairSpin`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L145).

> An ordered bond contributes at most one in absolute spin units.

```lean
lemma abs_pairSpin (I : IsingModel g) (σ : I.Configuration) (x y : X) :
    |I.pairSpin σ x y| = if g.Adj x y then 1 else 0
```

**`CondensedMatter.IsingModel.abs_sum_pairSpin_le`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L151).

> The total exchange spin sum is bounded by the number of connections between the regions.

```lean
lemma abs_sum_pairSpin_le (I : IsingModel g) (Λ M : Finset X)
    (σ : I.Configuration) :
    |∑ x ∈ Λ, ∑ y ∈ M, I.pairSpin σ x y| ≤ g.bondCountBetween Λ M
```

**`CondensedMatter.IsingModel.abs_energy_union_sub_le`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L164).

> Failure of energy additivity is controlled solely by the bonds crossing the boundary.

```lean
lemma abs_energy_union_sub_le [DecidableEq X] (I : IsingModel g)
    (Λ M : Finset X) (hΛM : Disjoint Λ M) (σ : I.Configuration) :
    |I.energy (Λ ∪ M) σ - I.energy Λ σ - I.energy M σ| ≤
      |I.J| * g.bondCountBetween Λ M
```

## D. Energy growth with volume

> A bounded coordination number ensures that the energy of every spin configuration grows
> at most linearly with the number of sites. The bound holds for either sign of exchange
> coupling and field.

**`CondensedMatter.IsingModel.abs_energy_le`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L183).

> The absolute energy is bounded by the internal bond count and the number of spins.

```lean
lemma abs_energy_le (I : IsingModel g) (Λ : Finset X) (σ : I.Configuration) :
    |I.energy Λ σ| ≤ |I.J| / 2 * g.bondCountBetween Λ Λ + |I.h| * Λ.card
```

**`CondensedMatter.IsingModel.abs_energy_le_of_degree_le`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L204).

> A coordination bound gives a uniform energy bound proportional to the region's volume.

```lean
lemma abs_energy_le_of_degree_le [g.LocallyFinite] (I : IsingModel g) (Λ : Finset X)
    (σ : I.Configuration) (q : ℕ) (hq : ∀ x ∈ Λ, (g.neighborFinset x).card ≤ q) :
    |I.energy Λ σ| ≤ (|I.J| * q / 2 + |I.h|) * Λ.card
```

## E. Ferromagnetic ground states

> For nonnegative exchange coupling, uniform polarization simultaneously minimizes every
> bond interaction. Alignment with the field also minimizes every one-site contribution.
> The minimum energy therefore depends only on the internal connections and the volume.

**`CondensedMatter.IsingModel.IsGroundState`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L225).

> A configuration minimizing the energy of the finite region `Λ`.
> Only interactions internal to the region enter this definition.

```lean
def IsGroundState (I : IsingModel g) (Λ : Finset X) (σ : I.Configuration) : Prop
```

**`CondensedMatter.IsingModel.polarized`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L229).

> Uniform spins aligned with the field; at zero field the up orientation is chosen.

```lean
noncomputable def polarized (I : IsingModel g) : I.Configuration
```

**`CondensedMatter.IsingModel.groundEnergy`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L233).

> The least finite-region energy over all spin configurations.

```lean
noncomputable def groundEnergy (I : IsingModel g) (Λ : Finset X) : ℝ
```

**`CondensedMatter.IsingModel.groundEnergy_eq_of_isGroundState`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L237).

> An energy-minimizing configuration attains the least energy.

```lean
lemma groundEnergy_eq_of_isGroundState (I : IsingModel g) (Λ : Finset X)
    {σ : I.Configuration} (hσ : I.IsGroundState Λ σ) :
    I.groundEnergy Λ = I.energy Λ σ
```

**`CondensedMatter.IsingModel.energy_polarized`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L244).

> Uniform field-aligned polarization has saturated exchange and field contributions.

```lean
lemma energy_polarized (I : IsingModel g) (Λ : Finset X) :
    I.energy Λ I.polarized =
      -(I.J / 2) * g.bondCountBetween Λ Λ - |I.h| * Λ.card
```

**`CondensedMatter.IsingModel.energy_lower_bound`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L263).

> Ferromagnetic energies cannot lie below the saturated exchange and field contributions.

```lean
lemma energy_lower_bound (I : IsingModel g) (hJ : 0 ≤ I.J) (Λ : Finset X)
    (σ : I.Configuration) :
    -(I.J / 2) * g.bondCountBetween Λ Λ - |I.h| * Λ.card ≤ I.energy Λ σ
```

**`CondensedMatter.IsingModel.isGroundState_polarized`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L272).

> Uniform field-aligned polarization is a ground state on every finite ferromagnetic region.

```lean
lemma isGroundState_polarized (I : IsingModel g) (hJ : 0 ≤ I.J) (Λ : Finset X) :
    I.IsGroundState Λ I.polarized
```

**`CondensedMatter.IsingModel.groundEnergy_eq`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L279).

> The exact ferromagnetic minimum counts internal bonds and field-aligned spins.

```lean
lemma groundEnergy_eq (I : IsingModel g) (hJ : 0 ≤ I.J) (Λ : Finset X) :
    I.groundEnergy Λ = -(I.J / 2) * g.bondCountBetween Λ Λ - |I.h| * Λ.card
```

## F. Ground-state energy per site

> The average internal coordination counts neighbors that remain in the region, averaged
> over its sites. If this average converges along nonempty regions, the ferromagnetic
> minimum energy per site converges with it. No regular degree, periodicity or prescribed
> shape of region is required.

**`CondensedMatter.IsingModel.groundEnergyDensity`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L292).

> The minimum finite-region energy divided by the number of sites.

```lean
noncomputable def groundEnergyDensity (I : IsingModel g) (Λ : Finset X) : ℝ
```

**`CondensedMatter.IsingModel.groundEnergyDensity_eq`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L296).

> The ferromagnetic minimum per site is determined by average internal coordination.

```lean
lemma groundEnergyDensity_eq (I : IsingModel g) (hJ : 0 ≤ I.J) (Λ : Finset X)
    (hΛ : Λ.Nonempty) :
    I.groundEnergyDensity Λ =
      -(I.J / 2) * ((g.bondCountBetween Λ Λ : ℝ) / Λ.card) - |I.h|
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L306).

> Convergent average internal coordination gives a ferromagnetic ground-state energy density.
> The statement applies to any sequence of nonempty finite regions on any graph.

```lean
lemma tendsto_groundEnergyDensity (I : IsingModel g) (hJ : 0 ≤ I.J)
    (Λ : ℕ → Finset X) (hΛ : ∀ n, (Λ n).Nonempty) (z : ℝ)
    (hz : Filter.Tendsto
      (fun n => (g.bondCountBetween (Λ n) (Λ n) : ℝ) / (Λ n).card)
      Filter.atTop (nhds z)) :
    Filter.Tendsto (fun n => I.groundEnergyDensity (Λ n))
      Filter.atTop (nhds (-(I.J / 2) * z - |I.h|))
```

## G. Crystal translation symmetry

**`CondensedMatter.IsingModel.translate`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L323).

> Transport a configuration along a crystal translation.

```lean
def translate (I : IsingModel g.toSimpleGraph) (a : G) (σ : I.Configuration) : I.Configuration
```

**`CondensedMatter.IsingModel.translate_apply`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L327).

> A transported spin has the same value at the transported site.

```lean
lemma translate_apply (I : IsingModel g.toSimpleGraph) (a : G)
    (σ : I.Configuration) (x : C.Site) : I.translate a σ (a +ᵥ x) = σ x
```

**`CondensedMatter.IsingModel.translateRegion`**, a def, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L332).

> Translate a finite region by the existing bijective action on crystal sites.

```lean
def translateRegion (a : G) (Λ : Finset C.Site) : Finset C.Site
```

**`CondensedMatter.IsingModel.pairSpin_translate`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L336).

> Exchange contributions are unchanged by translating both spins and sites.

```lean
lemma pairSpin_translate (I : IsingModel g.toSimpleGraph) (a : G) (σ : I.Configuration)
    (x y : C.Site) :
    I.pairSpin (I.translate a σ) (a +ᵥ x) (a +ᵥ y) = I.pairSpin σ x y
```

**`CondensedMatter.IsingModel.energy_translate`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean#L344).

> Uniform Ising interactions inherit the crystal's translation symmetry. Translating the
> region as well as its configuration preserves its energy.

```lean
lemma energy_translate (I : IsingModel g.toSimpleGraph) (a : G)
    (Λ : Finset C.Site) (σ : I.Configuration) :
    I.energy (translateRegion a Λ) (I.translate a σ) = I.energy Λ σ
```

## Depends on

- [Crystal bonds and connectivity](../crystal/part-01/graph.md)

## Sources

- [PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Basic.lean)
