---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.NatPair.K, Cslib.Complexity.PolynomialEncoding.NatPair.Lab, Cslib.Complexity.PolynomialEncoding.NatPair.pairEmb, Cslib.Complexity.PolynomialEncoding.NatPair.normEmb, Cslib.Complexity.PolynomialEncoding.NatPair.pairLabel, Cslib.Complexity.PolynomialEncoding.NatPair.normLabel, Cslib.Complexity.PolynomialEncoding.NatPair.prog, Cslib.Complexity.PolynomialEncoding.NatPair.st
statement: formalized
proof: formalized
---

# Projecting and normalizing a pair of binary naturals

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html).

## Stacks of the number-pair projector

Pair workspace, one reusable Nat buffer, and two canonical outputs.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#k).

## Control labels of the number-pair projector

Pair projection followed by normalization of the two fields.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#lab).

## Pair-frame splitter stack embedding in the number-pair projector

The pair-frame component acts only on its three own stacks.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.pairEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#pair-emb).

## Field-normalizer stack embedding in the number-pair projector

Each normalizer consumes its raw field, sharing only an empty buffer.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.normEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#norm-emb).

## Pair-frame splitter halt redirection in the number-pair projector

Only actual pair halt labels are redirected.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.pairLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#pair-label).

## Label map chaining the two field normalizers

Normalizing the first field continues with the second.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.normLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#norm-label).

## Program of the number-pair projector

All work is performed by the two existing finite components.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#prog).

## Six-stack invariant of the number-pair projector

Explicit six-stack invariant.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#st).

## Number-pair projector normalizes both fields of a raw pair frame

Every raw pair frame is projected and normalized without changing
the total Nat decoding semantics. Previous output suffixes survive.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.run_delimit`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#run-delimit).

## Decoding a pair of naturals fails exactly on a malformed first frame

Pair Nat decoding fails exactly when the first frame is malformed;
both raw field payloads use Mathlib's total Nat decoder.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.decode_pair_nat`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#decode-pair-nat).

## Number-pair projector yields both canonical payloads on success

A successful pair decode produces both canonical binary payloads,
with all scratch empty and arbitrary previous output suffixes preserved.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#run-some).

## Number-pair projector fails on malformed framing in linear time

Malformed pair framing fails in linear time. Private partial
workspace contents must be cleared before another invocation.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#run-none).

## Number-pair projector as a host component

The concrete two-Nat projector in the existing Host interface.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#component).

## Canonical payloads of a decoded pair are bounded by the raw input

Canonical output payload sizes are bounded by the raw input size,
even when either field had a noncanonical final zero bit.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.decoded_payload_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#decoded-payload-length-le).

## Number-pair projector reaches the decoding outcome

Total decoder outcome with exact successful output and empty
private scratch. Failure does not promise reusable workspace contents.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#run).

## Embedded number-pair projector preserves outside stacks

Callers may embed this concrete projector without disturbing
outside stacks. A failed workspace must be cleared before reuse.

Formalized by `Cslib.Complexity.PolynomialEncoding.NatPair.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/NatPair.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Projecting and normalizing a pair of binary naturals](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/projecting-and-normalizing-a-pair-of-binary-natu)
