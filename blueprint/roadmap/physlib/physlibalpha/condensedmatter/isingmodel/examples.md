---
declaration: module
origin: cited
lean: CondensedMatter.IsingModel.hypercubic, CondensedMatter.IsingModel.square, CondensedMatter.IsingModel.honeycomb, CondensedMatter.IsingModel.Hypercube.cells, CondensedMatter.IsingModel.Hypercube.mem_cells, CondensedMatter.IsingModel.Hypercube.card_cells, CondensedMatter.IsingModel.Hypercube.interior, CondensedMatter.IsingModel.Hypercube.mem_interior
statement: formalized
proof: formalized
---

# Classical Ising models on standard crystals

The module `PhyslibAlpha.CondensedMatter.IsingModel.Examples`, [PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean): 33 declarations, 26 with a docstring.

## i. Overview

> Uniform exchange and field parameters turn the existing crystal bond graphs into classical
> Ising models. The hypercubic model works in arbitrary dimension; the square lattice is its
> two-dimensional specialization. Honeycomb uses the same energy definition with its three
> bonds per site. Geometry plays no role in either construction.
>
> The main result concerns the ferromagnetic ground state of any crystal in `d` dimensions,
> with any number of sites per unit cell. Take a hypercube of `n + 1` unit cells along each
> lattice vector. Spins near its surface miss some of their neighbors, but they form a vanishing
> fraction of the sample as it grows. The ground-state energy per spin therefore converges to
> `-(J / 2) z̄ - |h|`, where `z̄` is the mean coordination of one unit cell: every spin
> contributes `-J` for half of its `z̄` bonds, and the aligned field contributes `-|h|`.
> The square lattice (`z̄ = 4`) and the honeycomb lattice (`z̄ = 3`) are instances.

## ii. Key results

> - `IsingModel.hypercubic`, `IsingModel.square`, `IsingModel.honeycomb` : uniform Ising models on
>   the standard bond graphs.
> - `IsingModel.Hypercube.tendsto_averageCoordination` : surface spins form a vanishing fraction of a
>   growing hypercube of cells.
> - `IsingModel.tendsto_groundEnergyDensity_hypercube` : the ferromagnetic ground-state energy per
>   spin of any crystal converges to `-(J / 2) z̄ - |h|`.
> - `IsingModel.tendsto_groundEnergyDensity_square`, `..._honeycomb` : the square and honeycomb
>   lattices.
> - `IsingModel.tendsto_groundEnergyDensity_of_card` : the density for a crystal in which every
>   site has `q` neighbours, with the diamond, fcc, bcc and hcp lattices as instances.

## iv. References

> * E. Ising, Beitrag zur Theorie des Ferromagnetismus.

## A. Ising models on the standard crystals

**`CondensedMatter.IsingModel.hypercubic`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L63).

> Uniform classical Ising interactions on the hypercubic bond graph in arbitrary dimension.

```lean
def hypercubic (d : ℕ) (J h : ℝ) : IsingModel (Crystal.hypercubicGraph d).toSimpleGraph
```

**`CondensedMatter.IsingModel.square`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L67).

> The square-lattice model, specializing the hypercubic construction to two dimensions.

```lean
def square (J h : ℝ) : IsingModel Crystal.squareGraph.toSimpleGraph
```

**`CondensedMatter.IsingModel.honeycomb`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L71).

> The honeycomb classical Ising model, using the crystal's existing bonds.

```lean
def honeycomb (J h : ℝ) : IsingModel Crystal.honeycombGraph.toSimpleGraph
```

## B. Hypercubes of unit cells in an arbitrary crystal

**`CondensedMatter.IsingModel.Hypercube.cells`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L83).

> The cells `{0, …, n}^d` of a hypercube of side `n + 1` unit cells.

```lean
def cells (d n : ℕ) : Finset (Fin d → ℤ)
```

**`CondensedMatter.IsingModel.Hypercube.mem_cells`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L86).

```lean
lemma mem_cells {d n : ℕ} (c : Fin d → ℤ) :
    c ∈ cells d n ↔ ∀ i, 0 ≤ c i ∧ c i ≤ n
```

**`CondensedMatter.IsingModel.Hypercube.card_cells`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L90).

```lean
lemma card_cells (d n : ℕ) : (cells d n).card = (n + 1) ^ d
```

**`CondensedMatter.IsingModel.Hypercube.interior`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L94).

> The cells at least `R` unit cells away from every face of the hypercube.

```lean
def interior (d n R : ℕ) : Finset (Fin d → ℤ)
```

**`CondensedMatter.IsingModel.Hypercube.mem_interior`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L97).

```lean
lemma mem_interior {d n R : ℕ} (c : Fin d → ℤ) :
    c ∈ interior d n R ↔ ∀ i, (R : ℤ) ≤ c i ∧ c i ≤ n - R
```

**`CondensedMatter.IsingModel.Hypercube.card_interior`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L102).

> The interior of a hypercube of side `n + 1` is a hypercube of side `n + 1 - 2 R`.

```lean
lemma card_interior (d n R : ℕ) : (interior d n R).card = (n + 1 - 2 * R) ^ d
```

**`CondensedMatter.IsingModel.Hypercube.interior_subset`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L106).

```lean
lemma interior_subset {d n R : ℕ} : interior d n R ⊆ cells d n
```

**`CondensedMatter.IsingModel.Hypercube.region`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L115).

> All sites of the crystal with unit cell labels `F` that lie in the cells `B`.

```lean
def region (B : Finset (Fin d → ℤ)) : Finset (Crystal.ofUnitCell (Fin d → ℤ) F).Site
```

**`CondensedMatter.IsingModel.Hypercube.mem_region`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L119).

```lean
lemma mem_region {B : Finset (Fin d → ℤ)} (x : (Crystal.ofUnitCell (Fin d → ℤ) F).Site) :
    x ∈ region B ↔ x.cell ∈ B
```

**`CondensedMatter.IsingModel.Hypercube.sum_region`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L125).

```lean
lemma sum_region {M : Type*} [AddCommMonoid M] {B : Finset (Fin d → ℤ)}
    (f : (Crystal.ofUnitCell (Fin d → ℤ) F).Site → M) :
    ∑ x ∈ region B, f x = ∑ c ∈ B, ∑ i : F, f ⟨c, i⟩
```

**`CondensedMatter.IsingModel.Hypercube.card_region`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L131).

```lean
lemma card_region (B : Finset (Fin d → ℤ)) :
    (region (F := F) B).card = B.card * Fintype.card F
```

**`CondensedMatter.IsingModel.Hypercube.region_cells_nonempty`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L136).

> Every hypercube contains at least one site if the unit cell does.

```lean
lemma region_cells_nonempty [Nonempty F] (d n : ℕ) :
    (region (F := F) (cells d n)).Nonempty
```

**`CondensedMatter.IsingModel.Hypercube.exists_range`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L147).

> Bonds have a finite range: there is a distance `R`, in units of the cell spacing, beyond
> which no two sites are connected. This holds because the coordination is finite and every
> site is a translate of one of finitely many reference sites.

```lean
lemma exists_range :
    ∃ R : ℕ, ∀ x y : (Crystal.ofUnitCell (Fin d → ℤ) F).Site,
      g.toSimpleGraph.Adj x y → ∀ k, |y.cell k - x.cell k| ≤ R
```

**`CondensedMatter.IsingModel.Hypercube.neighbors_subset_region`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L177).

> Sites in the interior of a hypercube have all their neighbors in the sample, once
> the interior is at least the bond range away from the surface.

```lean
lemma neighbors_subset_region {n R : ℕ}
    (hR : ∀ x y : (Crystal.ofUnitCell (Fin d → ℤ) F).Site,
      g.toSimpleGraph.Adj x y → ∀ k, |y.cell k - x.cell k| ≤ R)
    {x : (Crystal.ofUnitCell (Fin d → ℤ) F).Site} (hx : x.cell ∈ interior d n R) :
    g.neighbors x ⊆ region (cells d n)
```

**`CondensedMatter.IsingModel.Hypercube.meanCoordination`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L192).

> The mean number of neighbors per site of a crystal with unit cell `F`: the coordination
> averaged over the sites of one unit cell.

```lean
noncomputable def meanCoordination : ℝ
```

**`CondensedMatter.IsingModel.Hypercube.sum_card_neighbors_region`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L197).

> Summing the coordination over the sites of a set of cells counts every unit-cell
> coordination once per cell.

```lean
lemma sum_card_neighbors_region (B : Finset (Fin d → ℤ)) :
    ∑ x ∈ region B, (g.neighbors x).card =
      B.card * ∑ i : F, (g.neighbors ⟨0, i⟩).card
```

**`CondensedMatter.IsingModel.Hypercube.bondCountBetween_le`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L207).

> The ordered bonds inside a region number at most the total coordination of its sites.

```lean
lemma bondCountBetween_le (Λ : Finset (Crystal.ofUnitCell (Fin d → ℤ) F).Site) :
    g.toSimpleGraph.bondCountBetween Λ Λ ≤ ∑ x ∈ Λ, (g.neighbors x).card
```

**`CondensedMatter.IsingModel.Hypercube.sum_interior_le_bondCountBetween`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L214).

> Every site in the interior of the hypercube has all its bonds inside the hypercube.

```lean
lemma sum_interior_le_bondCountBetween {n R : ℕ}
    (hR : ∀ x y : (Crystal.ofUnitCell (Fin d → ℤ) F).Site,
      g.toSimpleGraph.Adj x y → ∀ k, |y.cell k - x.cell k| ≤ R) :
    ∑ x ∈ region (F := F) (interior d n R), (g.neighbors x).card ≤
      g.toSimpleGraph.bondCountBetween (region (cells d n)) (region (cells d n))
```

**`CondensedMatter.IsingModel.Hypercube.tendsto_averageCoordination`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L234).

> The average coordination of hypercubes converges to the mean coordination of the
> crystal: the sites near the surface, whose neighbors are cut off, become a vanishing fraction
> of the sample.

```lean
lemma tendsto_averageCoordination :
    Filter.Tendsto
      (fun n : ℕ => (g.toSimpleGraph.bondCountBetween (region (cells d n))
        (region (cells d n)) : ℝ) / (region (F := F) (cells d n)).card)
      Filter.atTop (nhds (meanCoordination g))
```

## C. Ground-state energy density of a ferromagnetic crystal

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_hypercube`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L307).

> The ground-state energy per spin of a ferromagnetic Ising model on any crystal, in
> hypercubes of growing size, converges to `-(J / 2) z̄ - |h|`, where `z̄` is the mean
> coordination. Each spin carries the energy `-J` for half of its bonds; the missing bonds
> at the surface of the sample do not contribute in the limit. The field may have either
> sign, and the lattice may have several sites per unit cell.

```lean
lemma tendsto_groundEnergyDensity_hypercube (I : IsingModel g.toSimpleGraph) (hJ : 0 ≤ I.J) :
    Filter.Tendsto (fun n : ℕ => I.groundEnergyDensity (region (cells d n)))
      Filter.atTop (nhds (-(I.J / 2) * meanCoordination g - |I.h|))
```

**`CondensedMatter.IsingModel.meanCoordination_honeycomb`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L316).

> The honeycomb lattice has three neighbors per site.

```lean
lemma meanCoordination_honeycomb : Hypercube.meanCoordination Crystal.honeycombGraph = 3
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_honeycomb`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L328).

> The ground-state energy per spin of the ferromagnetic honeycomb Ising model converges to
> `-3 J / 2 - |h|` as the sample grows.

```lean
lemma tendsto_groundEnergyDensity_honeycomb (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (honeycomb J h).groundEnergyDensity
        (Hypercube.region (Hypercube.cells 2 n)))
      Filter.atTop (nhds (-(3 * J / 2) - |h|))
```

**`CondensedMatter.IsingModel.meanCoordination_square`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L340).

> The square lattice has four neighbors per site.

```lean
lemma meanCoordination_square : Hypercube.meanCoordination Crystal.squareGraph = 4
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_square`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L348).

> The ground-state energy per spin of the ferromagnetic square-lattice Ising model
> converges to `-2 J - |h|` as the sample grows.

```lean
lemma tendsto_groundEnergyDensity_square (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (square J h).groundEnergyDensity
        (Hypercube.region (Hypercube.cells 2 n)))
      Filter.atTop (nhds (-(2 * J) - |h|))
```

## D. Regular crystals

**`CondensedMatter.IsingModel.meanCoordination_of_card`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L366).

> If every site has `q` neighbors, the mean coordination is `q`.

```lean
lemma meanCoordination_of_card {q : ℕ} (h : ∀ x, (g.neighbors x).card = q) :
    Hypercube.meanCoordination g = q
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_of_card`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L374).

> **The ferromagnetic ground-state energy density of a `q`-regular crystal** converges to
> `-q J / 2 - |h|`.

```lean
lemma tendsto_groundEnergyDensity_of_card {q : ℕ} (h : ∀ x, (g.neighbors x).card = q)
    (I : IsingModel g.toSimpleGraph) (hJ : 0 ≤ I.J) :
    Filter.Tendsto (fun n : ℕ => I.groundEnergyDensity (Hypercube.region (Hypercube.cells d n)))
      Filter.atTop (nhds (-(q * I.J / 2) - |I.h|))
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_diamond`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L384).

> The diamond lattice has four neighbors per site.

```lean
lemma tendsto_groundEnergyDensity_diamond (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (⟨J, h⟩ : IsingModel Crystal.diamondGraph.toSimpleGraph
        ).groundEnergyDensity (Hypercube.region (Hypercube.cells 3 n)))
      Filter.atTop (nhds (-(4 * J / 2) - |h|))
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_fcc`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L393).

> The face-centred cubic lattice has twelve neighbors per site.

```lean
lemma tendsto_groundEnergyDensity_fcc (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (⟨J, h⟩ : IsingModel Crystal.fccGraph.toSimpleGraph
        ).groundEnergyDensity (Hypercube.region (Hypercube.cells 3 n)))
      Filter.atTop (nhds (-(12 * J / 2) - |h|))
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_bcc`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L401).

> The body-centred cubic lattice has eight neighbors per site.

```lean
lemma tendsto_groundEnergyDensity_bcc (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (⟨J, h⟩ : IsingModel Crystal.bccGraph.toSimpleGraph
        ).groundEnergyDensity (Hypercube.region (Hypercube.cells 3 n)))
      Filter.atTop (nhds (-(8 * J / 2) - |h|))
```

**`CondensedMatter.IsingModel.tendsto_groundEnergyDensity_hcp`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean#L409).

> The hexagonal close-packed crystal has twelve neighbors per site.

```lean
lemma tendsto_groundEnergyDensity_hcp (J h : ℝ) (hJ : 0 ≤ J) :
    Filter.Tendsto (fun n : ℕ => (⟨J, h⟩ : IsingModel Crystal.hcpGraph.toSimpleGraph
        ).groundEnergyDensity (Hypercube.region (Hypercube.cells 3 n)))
      Filter.atTop (nhds (-(12 * J / 2) - |h|))
```

## Depends on

- [Orthorhombic, cubic and hexagonal close-packed crystals](../crystal/part-01/examples-threedimensional.md)
- [Classical Ising interactions on a graph](basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/IsingModel/Examples.lean)
