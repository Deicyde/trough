---
catalog: module
lean: Montgomery.ScalarFft.bitreverse, Montgomery.ScalarFft.fft
statement: formalized
proof: formalized
---

# Radix-2 DIT FFT over eight-limb Montgomery elements (zero-import)

`CompPoly.Fields.Montgomery.ScalarFft`, in [CompPoly/Fields/Montgomery/ScalarFft.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/ScalarFft.lean), by Gregor Mitscha-Baude.

> An in-place radix-2 decimation-in-time FFT over `Limbs8` Montgomery residues: a bit-reversal
> permutation followed by `logN` rounds of butterflies against a precomputed Montgomery-form
> twiddle table.  Like the arithmetic in `CompPoly.Fields.Montgomery.Native64x8Defs`, the loop
> nest is generic over the modulus, taking `q` and `negInv` explicitly.
>
> As explained in `CompPoly.Fields.Montgomery.Native64x8Defs`, this module deliberately imports
> nothing beyond that (itself zero-import) module: downstream consumers put it into
> `precompileModules` native-compilation lanes, and `precompileModules` compiles the
> entire import closure — so the runtime definitions must not pull in mathlib.
>
> This module contains runtime definitions only; correctness specifications live downstream
> for now.

`Montgomery.ScalarFft.bitreverse` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/ScalarFft.lean#L35))

> Bit-reversal permutation index.

```lean
def bitreverse (n l : Nat) : Nat
```

`Montgomery.ScalarFft.fft` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/ScalarFft.lean#L45))

> In-place radix-2 DIT FFT over eight-limb Montgomery residues modulo `q`: bit-reversal
> permutation, then `logN` rounds of butterflies against the Montgomery-form twiddles `tw`.

```lean
def fft (q : Limbs8) (negInv : UInt64) (a0 : Array Limbs8) (tw : Array Limbs8)
    (logN : Nat) : Array Limbs8
```

## Depends on

- [Eight-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x8defs.md)

## Sources

- [CompPoly/Fields/Montgomery/ScalarFft.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/ScalarFft.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.ScalarFft.json)
