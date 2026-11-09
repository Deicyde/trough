---
declaration: theorem
origin: cited
lean: FreyCurve.isPeuRamifieeAt_odd_of_integralForm
statement: formalized
proof: formalized
---

# FreyCurve.isPeuRamifieeAt_odd_of_integralForm

```lean
open FreyPackage
namespace FreyCurve
theorem isPeuRamifieeAt_odd_of_integralForm (P : FreyPackage) {q : ℕ} [Fact q.Prime]
    (hq2 : q ≠ 2) : P.freyCurve.IsPeuRamifieeAt P.p q
```

*Quoted from [Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean#L8) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “peu ramifiee”, “finite at p”.

PROOF-PATH.md names it in [5. Level lowering](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`FreyCurve.isPeuRamifieeAt_odd_of_integralForm`, stated in [Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean#L8) and proved in [P2M/Sol/S_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `FreyCurve.isPeuRamifieeAt_odd_of_integralForm` in Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean#L8)
- [Proof of `FreyCurve.isPeuRamifieeAt_odd_of_integralForm` in P2M/Sol/S_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_FreyCurve_isPeuRamifieeAt_odd_of_integralForm.lean)
- [The repository's documentation page for `FreyCurve.isPeuRamifieeAt_odd_of_integralForm`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#FreyCurve.isPeuRamifieeAt_odd_of_integralForm)
