---
declaration: section
origin: cited
lean: Algebra.exists_hasStandardEtaleSurjectionOn_of_exists_unramified, Algebra.exists_etale_isIdempotentElem_surjective_of_isUnramifiedAt, Algebra.exists_etale_completeOrthogonalIdempotents_surjective_not_liesOver
statement: formalized
proof: formalized
---

# 10.152 Local structure of unramified ring maps

Section 10.152 of the Stacks Project, [Tag 0G1D](https://stacks.math.columbia.edu/tag/0G1D). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0395, a proposition

[Tag 0395](https://stacks.math.columbia.edu/tag/0395) in the Stacks Project.

**`Algebra.exists_hasStandardEtaleSurjectionOn_of_exists_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalStructure.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalStructure.lean#L258). The attribute's comment: “The conclusion's three items are Mathlib's `HasStandardEtaleSurjectionOn R g`, namely `∃ (P : StandardEtalePair R) (φ : P.Ring →ₐ[R] Localization.Away g), Surjective φ`. The hypothesis "unramified at `q`" is Definition 00UT (3) verbatim, `∃ g ∉ Q, Algebra.Unramified R (Localization.Away g)`, rather than Mathlib's hypothesis pair `[Algebra.FiniteType R S] [Algebra.IsUnramifiedAt R Q]`, which implies it but is not implied by it; so this is strictly more general than Mathlib's `Algebra.IsUnramifiedAt.exists_hasStandardEtaleSurjectionOn` and implies it. See the module docstring.”.

> **Stacks 0395.** Let `R → S` be a ring map and `q ⊂ S` a prime. If `R → S` is unramified at
> `q` — that is, if `R → S_g` is unramified for some `g ∈ S`, `g ∉ q` — then there are a `g ∈ S`,
> `g ∉ q`, a standard étale ring map `R → S'` and a surjective `R`-algebra map `S' → S_g`.

```lean
public theorem Algebra.exists_hasStandardEtaleSurjectionOn_of_exists_unramified {R : Type u}
    {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (Q : Ideal S) [Q.IsPrime]
    (hQ : ∃ g ∉ Q, Algebra.Unramified R (Localization.Away g)) :
    ∃ g ∉ Q, HasStandardEtaleSurjectionOn R g
```

## Tag 00UX, a lemma

[Tag 00UX](https://stacks.math.columbia.edu/tag/00UX) in the Stacks Project.

**`Algebra.exists_etale_isIdempotentElem_surjective_of_isUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/EtaleLocalStructure.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/EtaleLocalStructure.lean#L264). The attribute's comment: “The product decomposition `R' ⊗_R S = A × B` is given by an idempotent `e`, with `A = (R' ⊗[R] S)[1/e]`, as in Mathlib's `Algebra.exists_etale_isIdempotentElem_forall_liesOver_eq` (Tag 00UJ); `p'A` lying over `q` is read along `S → R' ⊗[R] S → A`. See the module docstring.”.

> **Étale local structure of a ring map unramified at a prime.** Let `S` be a finite type
> `R`-algebra and let `q` be a prime of `S` lying over the prime `p` of `R` at which `S` is
> unramified over `R`. There are an étale `R`-algebra `R'`, a prime `p'` of `R'` lying over `p` and
> an idempotent `e` of `R' ⊗[R] S` — the product decomposition `R' ⊗[R] S = A × B` with
> `A = (R' ⊗[R] S)[1/e]` and `B = (R' ⊗[R] S)[1/(1 - e)]` — such that `R' → A` is surjective and
> `p'A` is a prime of `A` lying over `p'` and, along `S → R' ⊗[R] S → A`, over `q`.

```lean
public theorem Algebra.exists_etale_isIdempotentElem_surjective_of_isUnramifiedAt
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    [Algebra.IsUnramifiedAt R q] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R')
      (p' : Ideal R') (_ : p'.IsPrime) (_ : p'.LiesOver p) (e : R' ⊗[R] S)
      (_ : IsIdempotentElem e),
      Function.Surjective (algebraMap R' (Localization.Away e)) ∧
      (p'.map (algebraMap R' (Localization.Away e))).IsPrime ∧
      (p'.map (algebraMap R' (Localization.Away e))).LiesOver p' ∧
      (p'.map (algebraMap R' (Localization.Away e))).comap
        ((algebraMap (R' ⊗[R] S) (Localization.Away e)).comp
          (Algebra.TensorProduct.includeRight : S →ₐ[R] R' ⊗[R] S).toRingHom) = q
```

## Tag 00UY, a lemma

[Tag 00UY](https://stacks.math.columbia.edu/tag/00UY) in the Stacks Project.

**`Algebra.exists_etale_completeOrthogonalIdempotents_surjective_not_liesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/LocalStructure.lean, line 770](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/LocalStructure.lean#L770). The attribute's comment: “The product decomposition is given by complete orthogonal idempotents `e : Fin (n + 1) → R' ⊗[R] S`, the factors being `(R' ⊗[R] S)[1/e i]`. The prime of `Aᵢ` lying over `p'` is named as the source names it, namely `p'Aᵢ`. See the module docstring.”.

> **Separating the points of a fibre of an unramified ring map** (Stacks 00UY). Let `S` be an
> unramified `R`-algebra and `p` a prime of `R`. There are an étale `R`-algebra `R'`, a prime `p'`
> of `R'` lying over `p`, and a decomposition `R' ⊗[R] S = A₁ × ⋯ × Aₙ × B` — given by complete
> orthogonal idempotents `e 0, …, e n`, with `Aᵢ = (R' ⊗[R] S)[1/e i]` and `B = (R' ⊗[R] S)[1/e n]`
> — such that each `R' → Aᵢ` is surjective, each `p'Aᵢ` is a prime of `Aᵢ` lying over `p'`, and no
> prime of `B` lies over `p'`.

```lean
public theorem Algebra.exists_etale_completeOrthogonalIdempotents_surjective_not_liesOver
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Algebra.Unramified R S]
    (p : Ideal R) [p.IsPrime] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R') (p' : Ideal R')
      (_ : p'.IsPrime) (_ : p'.LiesOver p) (n : ℕ) (e : Fin (n + 1) → R' ⊗[R] S)
      (_ : CompleteOrthogonalIdempotents e),
      (∀ i : Fin n, Function.Surjective (algebraMap R' (Localization.Away (e i.castSucc)))) ∧
      (∀ i : Fin n, (p'.map (algebraMap R' (Localization.Away (e i.castSucc)))).IsPrime) ∧
      (∀ i : Fin n, (p'.map (algebraMap R' (Localization.Away (e i.castSucc)))).LiesOver p') ∧
      ∀ q : Ideal (Localization.Away (e (Fin.last n))), q.IsPrime → ¬ q.LiesOver p'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.152, Tag 0G1D](https://stacks.math.columbia.edu/tag/0G1D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
