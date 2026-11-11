---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint
statement: formalized
proof: formalized
---

# TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint

Against a trace-free self-adjoint `T`, the polarization of `Q₀` pairs as
`tr (B(ψ, φ) T) = 2 Re⟪T ψ, φ⟫`: the formal adjoint of the derivative `B(ψ, ·)` of `Q₀` is
`T ↦ 2 T ψ`.

```lean
TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℂ E] [FiniteDimensional ℂ E] [CompleteSpace E]
  {T : E →L[ℂ] E} (hT : T ∈ TauCeti.traceFreeSelfAdjoint E) (ψ φ : E) :
  (LinearMap.trace ℂ E) (↑((TauCeti.SeibergWitten.quadraticEndPolar ψ) φ) * ↑T) =
    2 * ↑(inner ℂ (T ψ) φ).re
```

## Depends on

- [TauCeti.traceFreeSelfAdjoint](tauceti-tracefreeselfadjoint.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/TracePairing.html#TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/TracePairing.html#TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint)
- [Source of `TauCeti.SeibergWitten.trace_quadraticEndPolar_mul_of_mem_traceFreeSelfAdjoint` in TauCeti/Analysis/PDE/SeibergWitten/TracePairing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/SeibergWitten/TracePairing.lean#L107)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
