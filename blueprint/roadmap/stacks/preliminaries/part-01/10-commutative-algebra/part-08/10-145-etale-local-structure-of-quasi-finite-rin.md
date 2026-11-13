---
declaration: section
origin: cited
lean: Algebra.exists_etale_isIdempotentElem_quasiFiniteAt_five_properties, Algebra.exists_etale_completeOrthogonalIdempotents_finite_not_quasiFiniteAt, Algebra.exists_etale_completeOrthogonalIdempotents_finite_isPurelyInseparable
statement: formalized
proof: formalized
---

# 10.145 Étale local structure of quasi-finite ring maps

Section 10.145 of the Stacks Project, [Tag 0G1B](https://stacks.math.columbia.edu/tag/0G1B). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00UJ, a lemma

[Tag 00UJ](https://stacks.math.columbia.edu/tag/00UJ) in the Stacks Project.

**`Algebra.exists_etale_isIdempotentElem_quasiFiniteAt_five_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/QuasiFiniteProductDecomposition.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/QuasiFiniteProductDecomposition.lean#L154). The attribute's comment: “The decomposition `R' ⊗_R S = A × B` is given by an idempotent `e`, with `A = (R' ⊗[R] S)[1/e]` and `B = (R' ⊗[R] S)[1/(1 - e)]`; the primes of `A` in (3) and (4) are the primes of `R' ⊗[R] S` not containing `e`. Properties (1)–(4) are Mathlib's `Algebra.exists_etale_isIdempotentElem_forall_liesOver_eq`; (5) is the last conjunct.”.

> **Stacks 00UJ.** Let `S` be a finite type `R`-algebra and `q` a prime of `S` lying over the
> prime `p` of `R` such that `S` is quasi-finite at `q`. There are an étale `R`-algebra `R'`, a prime
> `p'` of `R'` lying over `p` and an idempotent `e` of `R' ⊗[R] S` — the product decomposition
> `R' ⊗[R] S = A × B` with `A = (R' ⊗[R] S)[1/e]` and `B = (R' ⊗[R] S)[1/(1 - e)]` — such that
> 1. `κ(p) → κ(p')` is bijective,
> 2. `A` is finite over `R'`,
> 3. there is exactly one prime `r` of `A` (a prime of `R' ⊗[R] S` not containing `e`) lying over
>    `p'`,
> 4. `r` lies over `q`, and
> 5. no prime of `B` lies over both `p'` and `q`.

```lean
theorem Algebra.exists_etale_isIdempotentElem_quasiFiniteAt_five_properties
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p] [Algebra.QuasiFiniteAt R q] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R') (P : Ideal R')
      (_ : P.IsPrime) (_ : P.LiesOver p) (e : R' ⊗[R] S) (_ : IsIdempotentElem e)
      (P' : Ideal (R' ⊗[R] S)) (_ : P'.IsPrime) (_ : P'.LiesOver P),
      Function.Bijective (Ideal.ResidueField.mapₐ p P (Algebra.ofId _ _) (P.over_def p)) ∧
      Module.Finite R' (Localization.Away e) ∧
      e ∉ P' ∧
      (∀ P'' : Ideal (R' ⊗[R] S), P''.IsPrime → P''.LiesOver P → e ∉ P'' → P'' = P') ∧
      P'.comap Algebra.TensorProduct.includeRight.toRingHom = q ∧
      ¬ ∃ Q : Ideal (Localization.Away (1 - e)), Q.IsPrime ∧ Q.LiesOver P ∧
        Q.comap ((algebraMap (R' ⊗[R] S) (Localization.Away (1 - e))).comp
          Algebra.TensorProduct.includeRight.toRingHom) = q
```

## Tag 00UK, a lemma

[Tag 00UK](https://stacks.math.columbia.edu/tag/00UK) in the Stacks Project.

**`Algebra.exists_etale_completeOrthogonalIdempotents_finite_not_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalStructure.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalStructure.lean#L561). The attribute's comment: “The product decomposition is given by complete orthogonal idempotents `e : Fin (n + 1) → R' ⊗[R] S`, the factors being `(R' ⊗[R] S)[1/e i]`, and the primes of a factor are named by the primes of `R' ⊗[R] S` avoiding the corresponding idempotent. See the module docstring.”.

> **Étale local structure of a finite type algebra along a fibre** (Stacks 00UK). Let `S` be a
> finite type `R`-algebra and `p` a prime of `R`. There are an étale `R`-algebra `R'`, a prime `p'`
> of `R'` lying over `p` with `κ(p) = κ(p')`, and a decomposition
> `R' ⊗[R] S = A₁ × ⋯ × Aₙ × B` — given by complete orthogonal idempotents `e 0, …, e n`, with
> `Aᵢ = (R' ⊗[R] S)[1/e i]` and `B = (R' ⊗[R] S)[1/e n]` — such that each `Aᵢ` is finite over `R'`
> and has exactly one prime `r i` lying over `p'`, while `R' → B` is quasi-finite at no prime lying
> over `p'`.

```lean
public theorem Algebra.exists_etale_completeOrthogonalIdempotents_finite_not_quasiFiniteAt
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (p : Ideal R) [p.IsPrime] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R') (p' : Ideal R')
      (_ : p'.IsPrime) (_ : p'.LiesOver p) (n : ℕ) (e : Fin (n + 1) → R' ⊗[R] S)
      (_ : CompleteOrthogonalIdempotents e) (r : Fin n → Ideal (R' ⊗[R] S))
      (_ : ∀ i, (r i).IsPrime) (_ : ∀ i, (r i).LiesOver p'),
      Function.Bijective (Ideal.ResidueField.mapₐ p p' (Algebra.ofId _ _) (p'.over_def p)) ∧
      (∀ i : Fin n, Module.Finite R' (Localization.Away (e i.castSucc))) ∧
      (∀ i : Fin n, e i.castSucc ∉ r i) ∧
      (∀ (i : Fin n) (q : Ideal (R' ⊗[R] S)), q.IsPrime → q.LiesOver p' →
        e i.castSucc ∉ q → q = r i) ∧
      ∀ (q : Ideal (R' ⊗[R] S)) [q.IsPrime], q.LiesOver p' → e (Fin.last n) ∉ q →
        ¬ Algebra.QuasiFiniteAt R' q
```

## Tag 00UL, a lemma

[Tag 00UL](https://stacks.math.columbia.edu/tag/00UL) in the Stacks Project.

**`Algebra.exists_etale_completeOrthogonalIdempotents_finite_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalStructure.lean, line 1115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/LocalStructure.lean#L1115). The attribute's comment: “The product decomposition is given by complete orthogonal idempotents `e : Fin (n + 1) → R' ⊗[R] S`, the factors being `(R' ⊗[R] S)[1/e i]`, and the primes of a factor are named by the primes of `R' ⊗[R] S` avoiding the corresponding idempotent. Unlike Tag 00UK this does not assert `κ(p) = κ(p')`, which the source's proof gives up in order to control the residue fields. See the module docstring.”.

> **Étale local structure of a finite type algebra along a fibre** (Stacks 00UL). Let `S` be a
> finite type `R`-algebra and `p` a prime of `R`. There are an étale `R`-algebra `R'`, a prime `p'`
> of `R'` lying over `p`, and a decomposition `R' ⊗[R] S = A₁ × ⋯ × Aₙ × B` — given by complete
> orthogonal idempotents `e 0, …, e n`, with `Aᵢ = (R' ⊗[R] S)[1/e i]` and `B = (R' ⊗[R] S)[1/e n]`
> — such that each `Aᵢ` is finite over `R'` and has exactly one prime `r i` lying over `p'`, each
> residue field extension `κ(r i)/κ(p')` is finite purely inseparable, and `R' → B` is quasi-finite
> at no prime lying over `p'`.

```lean
public theorem Algebra.exists_etale_completeOrthogonalIdempotents_finite_isPurelyInseparable
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (p : Ideal R) [p.IsPrime] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R') (p' : Ideal R')
      (_ : p'.IsPrime) (_ : p'.LiesOver p) (n : ℕ) (e : Fin (n + 1) → R' ⊗[R] S)
      (_ : CompleteOrthogonalIdempotents e) (r : Fin n → Ideal (R' ⊗[R] S))
      (_ : ∀ i, (r i).IsPrime) (_ : ∀ i, (r i).LiesOver p'),
      (∀ i : Fin n, Module.Finite R' (Localization.Away (e i.castSucc))) ∧
      (∀ i : Fin n, e i.castSucc ∉ r i) ∧
      (∀ (i : Fin n) (q : Ideal (R' ⊗[R] S)), q.IsPrime → q.LiesOver p' →
        e i.castSucc ∉ q → q = r i) ∧
      (∀ i : Fin n, letI := Localization.AtPrime.algebraOfLiesOver p' (r i)
        Module.Finite p'.ResidueField (r i).ResidueField ∧
          IsPurelyInseparable p'.ResidueField (r i).ResidueField) ∧
      ∀ (q : Ideal (R' ⊗[R] S)) [q.IsPrime], q.LiesOver p' → e (Fin.last n) ∉ q →
        ¬ Algebra.QuasiFiniteAt R' q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.145, Tag 0G1B](https://stacks.math.columbia.edu/tag/0G1B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
