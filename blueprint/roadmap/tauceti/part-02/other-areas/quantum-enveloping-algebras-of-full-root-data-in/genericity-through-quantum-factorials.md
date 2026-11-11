---
declaration: theorem
origin: cited
lean: TauCeti.forall_quantumFactorial_ne_zero_iff
statement: formalized
proof: formalized
---

# Genericity through quantum factorials

all quantum factorials `[n]_q!` are nonzero exactly
when `q` is a generic quantum parameter, that is, nonzero and not a root of unity.

```lean
TauCeti.forall_quantumFactorial_ne_zero_iff.{u_1} {K : Type u_1} [Field K] {q : K} :
  (∀ (n : ℕ), TauCeti.quantumFactorial q n ≠ 0) ↔ TauCeti.IsGenericQuantumParameter q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_quantumFactorial_ne_zero_iff`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.forall_quantumFactorial_ne_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_quantumFactorial_ne_zero_iff`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.forall_quantumFactorial_ne_zero_iff)
- [Source of `TauCeti.forall_quantumFactorial_ne_zero_iff` in TauCeti/QuantumGroups/QuantumInteger/Factorial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Factorial.lean#L141)
- [Tau Ceti roadmap status: Quantum enveloping algebras of full root data, integral forms and quantum Frobenius](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumEnvelopingAlgebras/STATUS.md)
