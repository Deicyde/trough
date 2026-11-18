---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.ball, CondensedMatter.Crystal.PeriodicGraph.self_mem_ball, CondensedMatter.Crystal.PeriodicGraph.ball_mono, CondensedMatter.Crystal.PeriodicGraph.mem_ball_add, CondensedMatter.Crystal.PeriodicGraph.mem_neighbors_smul_iff, CondensedMatter.Crystal.PeriodicGraph.mem_ball_smul_iff
statement: formalized
proof: formalized
---

# Balls in the bond graph of a crystal

The module `PhyslibAlpha.CondensedMatter.Crystal.Balls`, [PhyslibAlpha/CondensedMatter/Crystal/Balls.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean): 6 declarations, 4 with a docstring.

> The sites within a given number of bonds of a site, and their behaviour under symmetries.

## i. Overview

> The *ball* of radius `n` around a site is the set of sites reached by at most `n` bonds. It is a
> finite set, as every site has finitely many neighbours. A group acting on the sites and preserving
> the bonds carries balls to balls. Balls give the finite regions on which a finite-range
> interaction acts: the interactions of a region only reach its bond neighbours.

## ii. Key results

> - `PeriodicGraph.ball` : the sites within `n` bonds of a site.
> - `PeriodicGraph.mem_ball_add` : following `m` bonds and then `n` bonds stays within `m + n` bonds.
> - `PeriodicGraph.mem_ball_smul_iff` : bond preserving group actions carry balls to balls.

## iv. References

> * None.

## A. Balls

**`CondensedMatter.Crystal.PeriodicGraph.ball`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L50).

> The sites within `n` bonds of a site.

```lean
def ball : ℕ → C.Site → Finset C.Site
```

**`CondensedMatter.Crystal.PeriodicGraph.self_mem_ball`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L54).

```lean
lemma self_mem_ball (n : ℕ) (x : C.Site) : x ∈ g.ball n x
```

**`CondensedMatter.Crystal.PeriodicGraph.ball_mono`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L59).

```lean
lemma ball_mono {m n : ℕ} (h : m ≤ n) (x : C.Site) : g.ball m x ⊆ g.ball n x
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_ball_add`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L65).

> Following `m` bonds and then `n` bonds stays within `m + n` bonds.

```lean
lemma mem_ball_add {m n : ℕ} {a b c : C.Site} (hb : b ∈ g.ball n a) (hc : c ∈ g.ball m b) :
    c ∈ g.ball (m + n) a
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_neighbors_smul_iff`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L84).

> A group action preserving the bonds carries the neighbours of a site to the neighbours of
> its image.

```lean
lemma mem_neighbors_smul_iff (hH : ∀ (h : H) (x y : C.Site),
    g.toSimpleGraph.Adj (h • x) (h • y) ↔ g.toSimpleGraph.Adj x y) (h : H) (x y : C.Site) :
    h • y ∈ g.neighbors (h • x) ↔ y ∈ g.neighbors x
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_ball_smul_iff`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean#L90).

> A group action preserving the bonds carries balls to balls.

```lean
lemma mem_ball_smul_iff (hH : ∀ (h : H) (x y : C.Site),
    g.toSimpleGraph.Adj (h • x) (h • y) ↔ g.toSimpleGraph.Adj x y) (h : H) (n : ℕ)
    (x y : C.Site) : h • y ∈ g.ball n (h • x) ↔ y ∈ g.ball n x
```

## Depends on

- [Crystal bonds and connectivity](graph.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Balls.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Balls.lean)
