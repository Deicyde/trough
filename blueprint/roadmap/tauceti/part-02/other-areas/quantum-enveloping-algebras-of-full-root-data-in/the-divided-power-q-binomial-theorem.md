---
declaration: theorem
origin: cited
lean: TauCeti.inv_quantumFactorial_smul_add_pow
statement: formalized
proof: formalized
---

# The divided-power `q`-binomial theorem

if `y x = q² x y` and `[n]_q! ≠ 0`, then the
divided power `(x + y)^(n) = (x + y)^n / [n]_q!` expands as
`∑_k q^(k(n-k)) x^(k) y^(n-k)`, with `x^(k) = x^k / [k]_q!`.

```lean
TauCeti.inv_quantumFactorial_smul_add_pow.{u_1, u_2} {K : Type u_1} [Field K] {A : Type u_2}
  [Semiring A] [Algebra K A] {q : K} {x y : A} (h : y * x = q ^ 2 • (x * y)) {n : ℕ}
  (hn : TauCeti.quantumFactorial q n ≠ 0) :
  (TauCeti.quantumFactorial q n)⁻¹ • (x + y) ^ n =
    ∑ k ∈ Finset.range (n + 1),
      q ^ (k * (n - k)) •
        ((TauCeti.quantumFactorial q k)⁻¹ • x ^ k *
          (TauCeti.quantumFactorial q (n - k))⁻¹ • y ^ (n - k))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.inv_quantumFactorial_smul_add_pow`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.inv_quantumFactorial_smul_add_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.inv_quantumFactorial_smul_add_pow`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Factorial.html#TauCeti.inv_quantumFactorial_smul_add_pow)
- [Source of `TauCeti.inv_quantumFactorial_smul_add_pow` in TauCeti/QuantumGroups/QuantumInteger/Factorial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Factorial.lean#L212)
- [Tau Ceti roadmap status: Quantum enveloping algebras of full root data, integral forms and quantum Frobenius](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumEnvelopingAlgebras/STATUS.md)
