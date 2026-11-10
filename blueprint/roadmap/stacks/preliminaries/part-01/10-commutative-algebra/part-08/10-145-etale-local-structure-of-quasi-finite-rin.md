---
declaration: section
origin: cited
lean: Algebra.exists_etale_completeOrthogonalIdempotents_finite_not_quasiFiniteAt, Algebra.exists_etale_completeOrthogonalIdempotents_finite_isPurelyInseparable
statement: formalized
proof: formalized
---

# 10.145 Étale local structure of quasi-finite ring maps

Section 10.145 of the Stacks Project, [Tag 0G1B](https://stacks.math.columbia.edu/tag/0G1B). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00UK, a lemma

[Tag 00UK](https://stacks.math.columbia.edu/tag/00UK) in the Stacks Project.

**`Algebra.exists_etale_completeOrthogonalIdempotents_finite_not_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalStructure.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/LocalStructure.lean#L561). The attribute's comment: “The product decomposition is given by complete orthogonal idempotents `e : Fin (n + 1) → R' ⊗[R] S`, the factors being `(R' ⊗[R] S)[1/e i]`, and the primes of a factor are named by the primes of `R' ⊗[R] S` avoiding the corresponding idempotent. See the module docstring.”.

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

**`Algebra.exists_etale_completeOrthogonalIdempotents_finite_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/LocalStructure.lean, line 1115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/LocalStructure.lean#L1115). The attribute's comment: “The product decomposition is given by complete orthogonal idempotents `e : Fin (n + 1) → R' ⊗[R] S`, the factors being `(R' ⊗[R] S)[1/e i]`, and the primes of a factor are named by the primes of `R' ⊗[R] S` avoiding the corresponding idempotent. Unlike Tag 00UK this does not assert `κ(p) = κ(p')`, which the source's proof gives up in order to control the residue fields. See the module docstring.”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
