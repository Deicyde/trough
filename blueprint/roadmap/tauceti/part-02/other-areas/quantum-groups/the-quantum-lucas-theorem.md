---
declaration: theorem
origin: cited
lean: TauCeti.quantumBinomial_mul_add_mul_add, TauCeti.laurentEval_signedLaurentQuantumBinomial_mul_add_mul_add
statement: formalized
proof: formalized
---

# The quantum Lucas theorem

If `q²` is a primitive `l`-th root of unity, `n₀ < l` and
`k₀ < l`, then `[n₁ l + n₀ choose k₁ l + k₀]_q` equals
`q^(l(k₁ n₀ - n₁ k₀) + (n₁ + 1) k₁ l²) [n₀ choose k₀]_q (n₁ choose k₁)`.
The power of `q` is a sign `±1`, and it is `1` when `q` has odd order.

```lean
TauCeti.quantumBinomial_mul_add_mul_add.{u_1} {K : Type u_1} [Field K] {q : K} {l : ℕ}
  (hq : IsPrimitiveRoot (q ^ 2) l) (n₁ k₁ : ℕ) {n₀ k₀ : ℕ} (hn₀ : n₀ < l) (hk₀ : k₀ < l) :
  TauCeti.quantumBinomial q (n₁ * l + n₀) (k₁ * l + k₀) =
    q ^ (↑l * (↑k₁ * ↑n₀ - ↑n₁ * ↑k₀) + (↑n₁ + 1) * ↑k₁ * ↑l ^ 2) *
        TauCeti.quantumBinomial q n₀ k₀ *
      ↑(n₁.choose k₁)
```

## Depends on

- [TauCeti.signedLaurentQuantumBinomial](../quantum-enveloping-algebras-of-full-root-data-in/tauceti-signedlaurentquantumbinomial.md)

## Proof depends on

- [Cauchy's binomial theorem, in coefficient form](cauchys-binomial-theorem-in-coefficient-form.md)
- [Quantum factorials at a root of unity](../quantum-enveloping-algebras-of-full-root-data-in/quantum-factorials-at-a-root-of-unity.md)
- [TauCeti.laurentQuantumFactorial](../quantum-enveloping-algebras-of-full-root-data-in/tauceti-laurentquantumfactorial.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quantumBinomial_mul_add_mul_add`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Lucas.html#TauCeti.quantumBinomial_mul_add_mul_add).

## Other forms

**The quantum Lucas theorem for signed Laurent Gaussians.** Formalized in Tau Ceti as [`TauCeti.laurentEval_signedLaurentQuantumBinomial_mul_add_mul_add`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Laurent/Lucas.html#TauCeti.laurentEval_signedLaurentQuantumBinomial_mul_add_mul_add).

```lean
TauCeti.laurentEval_signedLaurentQuantumBinomial_mul_add_mul_add.{u_1} {K : Type u_1} [Field K]
  {ζ : Kˣ} {l : ℕ} (hζ : IsPrimitiveRoot (↑ζ ^ 2) l) (m₁ : ℤ) (r₁ : ℕ) {m₀ r₀ : ℕ} (hm₀ : m₀ < l)
  (hr₀ : r₀ < l) :
  (TauCeti.laurentEval ζ) (TauCeti.signedLaurentQuantumBinomial (m₁ * ↑l + ↑m₀) (r₁ * l + r₀)) =
    ↑ζ ^ (↑l * (↑r₁ * ↑m₀ - m₁ * ↑r₀) + (m₁ + 1) * ↑r₁ * ↑l ^ 2) *
        TauCeti.quantumBinomial (↑ζ) m₀ r₀ *
      ↑(Ring.choose m₁ r₁)
```

## Sources

- [Tau Ceti documentation: `TauCeti.quantumBinomial_mul_add_mul_add`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Lucas.html#TauCeti.quantumBinomial_mul_add_mul_add)
- [Source of `TauCeti.quantumBinomial_mul_add_mul_add` in TauCeti/QuantumGroups/QuantumInteger/Lucas.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Lucas.lean#L107)
