---
declaration: theorem
origin: cited
lean: Geometry.SimplicialComplex.exists_subdivision_extending
statement: formalized
proof: formalized
---

# Relative simplicial subdivision of a family of compact convex cells

Let `P i` be a
locally finite family of compact convex sets with pairwise disjoint intrinsic interiors, with
prescribed points `p i` of their intrinsic interiors, and let `L` be a simplicial complex meeting
every cell in a finite subcomplex and avoiding the intrinsic interiors of all cells. Suppose the
intrinsic frontier of each cell is covered by `|L|` and the other cells contained in it. Then
there is a simplicial complex `K` with `|K| = |L| ∪ ⋃ i, P i` which contains `L`, has no other
simplex with all its vertices in `|L|`, triangulates every cell by finitely many of its simplices,
and each of whose simplices outside `L` lies in a single cell `P i` and has `p i` as a vertex.

```lean
Geometry.SimplicialComplex.exists_subdivision_extending.{u_1, u_2} {E : Type u_1} {ι : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (L : Geometry.SimplicialComplex ℝ E) (P : ι → Set E) (hPc : ∀ (i : ι), IsCompact (P i))
  (hPv : ∀ (i : ι), Convex ℝ (P i)) (p : ι → E) (hp : ∀ (i : ι), p i ∈ intrinsicInterior ℝ (P i))
  (hPlf : LocallyFinite P)
  (hri : Pairwise fun i j => Disjoint (intrinsicInterior ℝ (P i)) (intrinsicInterior ℝ (P j)))
  (hfr : ∀ (i : ι), intrinsicFrontier ℝ (P i) ⊆ L.space ∪ ⋃ j, ⋃ (_ : j ≠ i ∧ P j ⊆ P i), P j)
  (hL : ∀ (i : ι), P i ∩ L.space ⊆ (L.restrict (P i)).space)
  (hLi : ∀ (i : ι), Disjoint (intrinsicInterior ℝ (P i)) L.space)
  (hLfin : ∀ (i : ι), (L.restrict (P i)).faces.Finite) :
  ∃ K,
    K.restrict L.space = L ∧
      K.space = L.space ∪ ⋃ i, P i ∧
        (∀ (i : ι), (K.restrict (P i)).space = P i ∧ (K.restrict (P i)).faces.Finite) ∧
          ∀ s ∈ K.faces, s ∈ L.faces ∨ ∃ i, p i ∈ s ∧ ↑s ⊆ P i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Geometry.SimplicialComplex.exists_subdivision_extending`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Subdivision.html#Geometry.SimplicialComplex.exists_subdivision_extending).

## Sources

- [Tau Ceti documentation: `Geometry.SimplicialComplex.exists_subdivision_extending`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Subdivision.html#Geometry.SimplicialComplex.exists_subdivision_extending)
- [Source of `Geometry.SimplicialComplex.exists_subdivision_extending` in TauCeti/Analysis/Convex/SimplicialComplex/Subdivision.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/SimplicialComplex/Subdivision.lean#L303)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
