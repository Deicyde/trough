---
catalog: module
lean: Montgomery.gcdBitLen, Montgomery.gcdInner
statement: formalized
proof: formalized
---

# Word-sized divsteps: runtime definitions (zero-import)

`CompPoly.Fields.Montgomery.DivstepDefs`, in [CompPoly/Fields/Montgomery/DivstepDefs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/DivstepDefs.lean), by Georgios Raikos.

> The word-sized divstep loop of the Pornin binary-GCD inversion
> ([eprint 2020/972](https://eprint.iacr.org/2020/972)) and its bit-length helper. Both act on
> single `UInt64` words, so they do not depend on the limb count of a Montgomery carrier. The
> multi-limb inversion runtimes call them on one-word approximations of their operands.
>
> This module has zero imports, for `precompileModules` consumers. The proof side is
> `Montgomery/Divstep`.

`Montgomery.gcdBitLen` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/DivstepDefs.lean#L25))

> Bit length of a word.

```lean
def gcdBitLen (x : UInt64) : Nat
```

`Montgomery.gcdInner` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/DivstepDefs.lean#L38))

> The word-sized divstep loop, accumulating the transition matrix; `b` must be odd.

```lean
def gcdInner (rounds : Nat) (a b : UInt64) (f0 g0 f1 g1 : Int) :
    UInt64 × UInt64 × Int × Int × Int × Int
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Montgomery/DivstepDefs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/DivstepDefs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.DivstepDefs.json)
