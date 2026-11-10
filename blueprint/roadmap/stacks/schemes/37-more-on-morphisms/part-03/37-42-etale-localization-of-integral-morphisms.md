---
declaration: section
origin: cited
lean: Algebra.exists_etale_completeOrthogonalIdempotents_integral_isPurelyInseparable
statement: formalized
proof: formalized
---

# 37.42 Étale localization of integral morphisms

Section 37.42 of the Stacks Project, [Tag 0BUH](https://stacks.math.columbia.edu/tag/0BUH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BSR, a lemma

[Tag 0BSR](https://stacks.math.columbia.edu/tag/0BSR) in the Stacks Project.

**`Algebra.exists_etale_completeOrthogonalIdempotents_integral_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/IntegralSplitting.lean, line 1285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Etale/IntegralSplitting.lean#L1285).

> **Splitting an integral algebra after an étale extension.**
> If an integral `R`-algebra `S` has finitely many primes over `p`, and the maximal separable
> subextension of every corresponding residue-field extension is finite, then after an étale base
> change the algebra splits into integral factors having one prime over the chosen prime and purely
> inseparable residue-field extensions.

```lean
public theorem exists_etale_completeOrthogonalIdempotents_integral_isPurelyInseparable
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.IsIntegral R S] (p : Ideal R) [p.IsPrime]
    (hfinite : Set.Finite {q : Ideal S | q.IsPrime ∧ q.LiesOver p})
    (hseparable : ∀ (q : Ideal S) (hq : q.IsPrime) (hqover : q.LiesOver p),
      letI := hq
      letI := hqover
      letI := Localization.AtPrime.algebraOfLiesOver p q
      Module.Finite p.ResidueField
        (separableClosure p.ResidueField q.ResidueField)) :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R') (_ : Algebra.Etale R R')
      (p' : Ideal R') (_ : p'.IsPrime) (_ : p'.LiesOver p) (n : ℕ)
      (e : Fin n → R' ⊗[R] S) (_ : CompleteOrthogonalIdempotents e)
      (r : (i : Fin n) → Ideal (Localization.Away (e i)))
      (_ : ∀ i, (r i).IsPrime) (_ : ∀ i, (r i).LiesOver p'),
      (∀ i : Fin n, Algebra.IsIntegral R' (Localization.Away (e i))) ∧
      (∀ (i : Fin n) (q : Ideal (Localization.Away (e i))),
        q.IsPrime → q.LiesOver p' → q = r i) ∧
      ∀ i : Fin n,
        letI := Localization.AtPrime.algebraOfLiesOver p' (r i)
        IsPurelyInseparable p'.ResidueField (r i).ResidueField
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.42, Tag 0BUH](https://stacks.math.columbia.edu/tag/0BUH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
