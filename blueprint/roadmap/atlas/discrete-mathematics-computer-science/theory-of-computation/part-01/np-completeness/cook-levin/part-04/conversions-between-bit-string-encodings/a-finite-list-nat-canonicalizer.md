---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.ListNatMachine.K, Cslib.Complexity.PolynomialEncoding.ListNatMachine.emb, Cslib.Complexity.PolynomialEncoding.ListNatMachine.Lab, Cslib.Complexity.PolynomialEncoding.ListNatMachine.natLabel, Cslib.Complexity.PolynomialEncoding.ListNatMachine.prog, Cslib.Complexity.PolynomialEncoding.ListNatMachine.st, Cslib.Complexity.PolynomialEncoding.ListNatMachine.element_run, Cslib.Complexity.PolynomialEncoding.ListNatMachine.blocks_run
statement: formalized
proof: formalized
---

# A finite List Nat canonicalizer

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html).

## Stacks of the list-of-naturals canonicalizer

External input, reverse accumulator, final output, and Nat workspace.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#k).

## Stack embedding of the number normalizer in the list canonicalizer

Only the Nat workspace is visible to the shared normalizer.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.emb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#emb).

## Control labels of the list-of-naturals canonicalizer

The normalizer's halt resumes frame emission.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#lab).

## Label embedding of the number normalizer in the list canonicalizer

Label embedding of the actual shared Nat normalizer.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.natLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#nat-label).

## Program of the list-of-naturals canonicalizer

The concrete canonicalizer program.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#prog).

## Workspace layout of the list-of-naturals canonicalizer

Workspace layout for the composition invariant.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#st).

## List canonicalizer normalizes one element

One list element is normalized and appended to the reverse
accumulator; every scratch stack is ready for the next call.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.element_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#element-run).

## List canonicalizer normalizes a sequence of framed payloads

Normalize any finite sequence of framed Nat payloads. The payloads
need not be canonical, and previous accumulator/output suffixes survive.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.blocks_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#blocks-run).

## List canonicalizer runs in linear time on decodable input

Successful raw List Nat decoding is implemented in linear time,
with canonical output and all private scratch stacks empty.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#run-some).

## List canonicalizer fails on malformed input

Every malformed raw List Nat input reaches the failure endpoint.
The accumulator and Nat output may contain partial data; clear the
workspace before reuse. No output claim is made for a failed parse.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#run-none).

## List-of-naturals canonicalizer as a host component

The List Nat canonicalizer uses the existing finite Host interface.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#component).

## List canonicalizer reaches the decoding outcome with canonical output

A total success/failure contract at the two actual halt labels.
Success has canonical output; failure exposes no partial-output promise.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#run).

## Embedded list canonicalizer preserves outside stacks

Embed the concrete normalizer in a caller, preserving every stack
outside its workspace on both success and failure. Entry requires clean
scratch and output stacks. After `bad`, clear partial workspace data
before another invocation.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatMachine.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatMachine.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A finite List Nat canonicalizer](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-finite-list-nat-canonicalizer)
