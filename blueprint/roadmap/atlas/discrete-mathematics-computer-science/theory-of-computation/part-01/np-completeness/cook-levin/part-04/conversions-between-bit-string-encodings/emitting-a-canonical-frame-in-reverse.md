---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.emitFrame, Cslib.Complexity.PolynomialEncoding.emitFrame_run
statement: formalized
proof: formalized
---

# Emitting a canonical frame in reverse

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/emitting-a-canonical-frame-in-reverse/index.html).

## Reversed self-delimiting frame emitter

Emit one raw payload as a reversed self-delimiting frame.

Formalized by `Cslib.Complexity.PolynomialEncoding.emitFrame`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Frame.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/Frame.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/emitting-a-canonical-frame-in-reverse/index.html#emit-frame).

## Frame emitter takes one step per payload bit plus one

Emit a complete frame in `payload.length + 1` steps, restoring the
input suffix and leaving every unrelated stack unchanged.

Formalized by `Cslib.Complexity.PolynomialEncoding.emitFrame_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Frame.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/Frame.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/emitting-a-canonical-frame-in-reverse/index.html#emit-frame-run).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Emitting a canonical frame in reverse](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/emitting-a-canonical-frame-in-reverse/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/emitting-a-canonical-frame-in-reverse)
