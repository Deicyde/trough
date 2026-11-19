---
declaration: def
origin: cited
lean: TauCeti.LFunctions.heckeLFunctionC
statement: formalized
---

# The presented Hecke L-function of a ray class character `χ` of `𝔪`

the canonical
meromorphic continuation from `Re s > 1` of the L-series of `χ`, summed over the ideals prime to
the finite part of `𝔪`. It depends on the presentation and not only on the character
(`heckeLFunctionC_induced`). It agrees with the L-series on `Re s > 1` once a continuation to the
plane exists (`meromorphicContinuation_eqOn`), and is `0` otherwise.

```lean
TauCeti.LFunctions.heckeLFunctionC.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {𝔪 : TauCeti.GlobalNumberFields.Modulus K} (χ : TauCeti.GlobalNumberFields.RayClassCharacter 𝔪) :
  ℂ → ℂ
```

## Depends on

- [TauCeti.meromorphicContinuation](tauceti-meromorphiccontinuation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.heckeLFunctionC`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Hecke/Basic.html#TauCeti.LFunctions.heckeLFunctionC).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.heckeLFunctionC`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Hecke/Basic.html#TauCeti.LFunctions.heckeLFunctionC)
- [Source of `TauCeti.LFunctions.heckeLFunctionC` in TauCeti/NumberTheory/LFunctions/Hecke/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Hecke/Basic.lean#L70)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
