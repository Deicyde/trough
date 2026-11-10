---
declaration: section
origin: cited
lean: Stacks.Intersection.ReductionToDiagonal.torFormulaCycleIntersectionProduct_assoc, Stacks.Intersection.finsum_alternating_length_tor_assoc_of_isRegularLocalRing, Stacks.Intersection.finsum_alternating_length_tor_assoc_quotient
statement: formalized
proof: formalized
---

# 43.20 Associativity of intersections

Section 43.20 of the Stacks Project, [Tag 0B1K](https://stacks.math.columbia.edu/tag/0B1K). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B1L, a lemma

[Tag 0B1L](https://stacks.math.columbia.edu/tag/0B1L) in the Stacks Project.

**`Stacks.Intersection.ReductionToDiagonal.torFormulaCycleIntersectionProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/SubvarietyProductAssociativity.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ReductionToDiagonal/SubvarietyProductAssociativity.lean#L615). The attribute's comment: “the whole lemma: `U · (V · W) = (U · V) · W` as cycles on `X`, for three closed subvarieties of a nonsingular variety over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — intersecting properly pairwise and satisfying the displayed dimension bound, together with the properness of the two outer intersections that the statement presupposes. Closed subvarieties are their generic points, so `U`, `V`, `W` are the reduced closures of three points and `[U]` is the prime cycle at `u`. The inner products `V · W` and `U · V` are the Section 43.14 product of Tag 0AZR in the integer expected dimensions `dim V + dim W - dim X` and `dim U + dim V - dim X`, and the outer products the bilinear extension of Tag 0B08 in dimension `dim U + dim V + dim W - 2 dim X`. `WithBot ℕ∞` has no subtraction, so the displayed bound is spelled `dim (U ∩ V ∩ W) + 2 dim X ≤ dim U + dim V + dim W`, as proper intersection is in Tag 0AZQ.”.

> **Stacks Project, Tag 0B1L.** Let `X` be a nonsingular variety over an algebraically closed
> field — the convention of the chapter, Tag 0AZ8 — of dimension `dX`, and let `U`, `V`, `W` be
> closed subvarieties, namely the reduced closures of three points `u`, `v`, `w`, of dimensions
> `r`, `s`, `t`. Assume `U`, `V`, `W` intersect properly pairwise and that
>
> `dim (U ∩ V ∩ W) ≤ dim U + dim V + dim W - 2 dim X`.
>
> Then `U` and `V · W` intersect properly, `U · V` and `W` intersect properly — so that the two
> iterated products are defined, as the source's statement presupposes — and, as cycles on `X`,
>
> `U · (V · W) = (U · V) · W`.
>
> Here `V · W` and `U · V` are the products of Section 43.14 (Tag 0AZR) in dimensions
> `s + t - dX` and `r + s - dX`, and the outer products are their bilinear extension of Tag 0B08 in
> dimension `r + s + t - 2 dX`; the three expected dimensions are integers, so that the
> configurations in which one of them is negative are included.

```lean
theorem torFormulaCycleIntersectionProduct_assoc [DecidableEq X] (k : Type u) [Field k]
    [IsAlgClosed k] (f : X ⟶ Spec (.of k)) [IsVariety k f] (hX : IsRegular X)
    (u v w : X) (dX r s t : ℕ)
    (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (hu : topologicalKrullDim (closure ({u} : Set X)) = (r : WithBot ℕ∞))
    (hv : topologicalKrullDim (closure ({v} : Set X)) = (s : WithBot ℕ∞))
    (hw : topologicalKrullDim (closure ({w} : Set X)) = (t : WithBot ℕ∞))
    (huv : AlgebraicGeometry.IntersectProperly
      ⟨closure {u}, isIrreducible_singleton.closure, isClosed_closure⟩
      ⟨closure {v}, isIrreducible_singleton.closure, isClosed_closure⟩)
    (hvw : AlgebraicGeometry.IntersectProperly
      ⟨closure {v}, isIrreducible_singleton.closure, isClosed_closure⟩
      ⟨closure {w}, isIrreducible_singleton.closure, isClosed_closure⟩)
    (_huw : AlgebraicGeometry.IntersectProperly
      ⟨closure {u}, isIrreducible_singleton.closure, isClosed_closure⟩
      ⟨closure {w}, isIrreducible_singleton.closure, isClosed_closure⟩)
    (huvw : topologicalKrullDim
        (↥(closure ({u} : Set X) ∩ closure ({v} : Set X) ∩ closure ({w} : Set X))) +
          ((2 * dX : ℕ) : WithBot ℕ∞) ≤ ((r + s + t : ℕ) : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    AlgebraicCycle.IntersectProperly (Function.locallyFinsuppWithin.single u (1 : ℤ))
        (torSubvarietyProductOfBound (fieldChowSituation k) f hX ((s : ℤ) + t - dX)
          (torSupportBound_of_intersectProperly_of_eq k f hX v w hdX hv hw hvw)) ∧
      AlgebraicCycle.IntersectProperly
        (torSubvarietyProductOfBound (fieldChowSituation k) f hX ((r : ℤ) + s - dX)
          (torSupportBound_of_intersectProperly_of_eq k f hX u v hdX hu hv huv))
        (Function.locallyFinsuppWithin.single w (1 : ℤ)) ∧
      torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + s + t - 2 * dX)
          (Function.locallyFinsuppWithin.single u 1)
          (torSubvarietyProductOfBound (fieldChowSituation k) f hX ((s : ℤ) + t - dX)
            (torSupportBound_of_intersectProperly_of_eq k f hX v w hdX hv hw hvw)) =
        torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + s + t - 2 * dX)
          (torSubvarietyProductOfBound (fieldChowSituation k) f hX ((r : ℤ) + s - dX)
            (torSupportBound_of_intersectProperly_of_eq k f hX u v hdX hu hv huv))
          (Function.locallyFinsuppWithin.single w 1)
```

**`Stacks.Intersection.finsum_alternating_length_tor_assoc_of_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TripleProductAssociativity.lean, line 1276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TripleProductAssociativity.lean#L1276). The attribute's comment: “the associativity `U · (V · W) = (U · V) · W` in local form at the local ring `A` of the ambient nonsingular variety at the generic point of a component of the triple intersection. By the Tor formula of Stacks 0B0W the coefficient of such a component in `U · (V · W)` is the alternating double sum `∑ᵢⱼ (-1)^(i+j) length_A Torᵢ^A(𝒪_U, Torⱼ^A(𝒪_V, 𝒪_W))` and its coefficient in `(U · V) · W` is the right-associated sum; what is proved here is that those two sums agree, for arbitrary finite `A`-modules in place of the three local rings whose supports meet only in the maximal ideal. That support condition is the local form of the source's hypotheses that `U`, `V`, `W` meet properly pairwise and that `dim (U ∩ V ∩ W) ≤ dim U + dim V + dim W - 2 dim X`, which the source uses for exactly this purpose: to bound the dimensions of the supports of the sheaves appearing in the two sums. Every length in the two sums is then finite, since a `Tor` module of finite modules over a Noetherian ring is finite by Stacks 0AZ4 and its support lies in the intersection of the two supports, so each iterated `Tor` module is a finite module supported in the maximal ideal. The identity of the two sums is the claim the source's proof establishes, by the double-complex spectral sequence of Homology Section 012X in the form of More on Algebra Example 0662 (in the library as `CochainComplex.DerivedTensorSpectralSequence.exists_derived_tensor_spectral_sequences`) together with the additivity of length on short exact sequences.”.

> **Stacks 0B1L: associativity of intersections, at a point.** Let `A` be a regular local ring
> of dimension at most `n` — the local ring of a nonsingular variety `X` at the generic point of a
> component `Z` of `U ∩ V ∩ W` — and let `M`, `N`, `P` be finite `A`-modules whose supports meet
> only in the maximal ideal, which is what it means for `Z` to be isolated in `U ∩ V ∩ W`. Then
>
> `∑ᵢⱼ (-1)ⁱ⁺ʲ length Torᵢᴬ(M, Torⱼᴬ(N, P)) = ∑ᵢⱼ (-1)ⁱ⁺ʲ length Torᵢᴬ(Torⱼᴬ(M, N), P)`,
>
> both sums being finite. For `M`, `N`, `P` the local rings of `U`, `V`, `W` the two sides are the
> coefficients of `Z` in `U · (V · W)` and in `(U · V) · W`.

```lean
theorem finsum_alternating_length_tor_assoc_of_isRegularLocalRing (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (M N P : ModuleCat.{u} A) [Module.Finite A M] [Module.Finite A N]
    [Module.Finite A P] (n : ℕ) (hdim : ringKrullDim A ≤ (n : WithBot ℕ∞))
    (hsupp : Module.support A M ∩ Module.support A N ∩ Module.support A P ⊆
      {IsLocalRing.closedPoint A}) :
    (∑ᶠ pq : ℕ × ℕ, (-1 : ℤ) ^ (pq.1 + pq.2) * ((Module.length A
        (((Tor (ModuleCat.{u} A) pq.1).obj M).obj
          (((Tor (ModuleCat.{u} A) pq.2).obj N).obj P))).toNat : ℤ))
      = ∑ᶠ pq : ℕ × ℕ, (-1 : ℤ) ^ (pq.1 + pq.2) * ((Module.length A
        (((Tor (ModuleCat.{u} A) pq.1).obj
          (((Tor (ModuleCat.{u} A) pq.2).obj M).obj N)).obj P)).toNat : ℤ)
```

**`Stacks.Intersection.finsum_alternating_length_tor_assoc_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TripleProductAssociativity.lean, line 1301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/TripleProductAssociativity.lean#L1301). The attribute's comment: “the associativity `U · (V · W) = (U · V) · W` in local form, for the three local rings `A ⧸ I`, `A ⧸ J`, `A ⧸ K` of the subvarieties at the generic point of a component of the triple intersection; the two sides are the coefficients of that component in the two iterated products, by the Tor formula of Stacks 0B0W. See `Stacks.Intersection.finsum_alternating_length_tor_assoc_of_isRegularLocalRing` for what is and is not carried.”.

> **Stacks 0B1L for three closed subvarieties, at a point.** The case of the three local rings
> `A ⧸ I`, `A ⧸ J`, `A ⧸ K` of closed subvarieties `U`, `V`, `W` cut out at the point by the
> ideals `I`, `J`, `K`: the two iterated alternating sums of lengths of `Tor` modules agree.

```lean
theorem finsum_alternating_length_tor_assoc_quotient (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (I J K : Ideal A) (n : ℕ)
    (hdim : ringKrullDim A ≤ (n : WithBot ℕ∞))
    (hfinL : ∀ p q : ℕ, Module.length A
      (((Tor (ModuleCat.{u} A) p).obj (ModuleCat.of A (A ⧸ I))).obj
        (((Tor (ModuleCat.{u} A) q).obj (ModuleCat.of A (A ⧸ J))).obj
          (ModuleCat.of A (A ⧸ K)))) ≠ ⊤)
    (hfinR : ∀ p q : ℕ, Module.length A
      (((Tor (ModuleCat.{u} A) p).obj
        (((Tor (ModuleCat.{u} A) q).obj (ModuleCat.of A (A ⧸ I))).obj
          (ModuleCat.of A (A ⧸ J)))).obj (ModuleCat.of A (A ⧸ K))) ≠ ⊤) :
    (∑ᶠ pq : ℕ × ℕ, (-1 : ℤ) ^ (pq.1 + pq.2) * ((Module.length A
        (((Tor (ModuleCat.{u} A) pq.1).obj (ModuleCat.of A (A ⧸ I))).obj
          (((Tor (ModuleCat.{u} A) pq.2).obj (ModuleCat.of A (A ⧸ J))).obj
            (ModuleCat.of A (A ⧸ K))))).toNat : ℤ))
      = ∑ᶠ pq : ℕ × ℕ, (-1 : ℤ) ^ (pq.1 + pq.2) * ((Module.length A
        (((Tor (ModuleCat.{u} A) pq.1).obj
          (((Tor (ModuleCat.{u} A) pq.2).obj (ModuleCat.of A (A ⧸ I))).obj
            (ModuleCat.of A (A ⧸ J)))).obj (ModuleCat.of A (A ⧸ K)))).toNat : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.20, Tag 0B1K](https://stacks.math.columbia.edu/tag/0B1K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
