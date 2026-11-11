---
declaration: section
origin: cited
lean: Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP, Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP_ciphertextDist_eq_uniform, Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP_perfectlySecret
statement: formalized
proof: formalized
---

# One-time pad over a finite group

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group/index.html).

## The group one-time pad

Let $G$ be a finite group. The group one-time pad on $G$ is the
private-key encryption scheme with messages, keys and ciphertexts in $G$ whose key $k$ is drawn
uniformly from $G$, which encrypts a message $m$ as $k m$, and which decrypts a ciphertext $c$
as $k^{-1} c$.

Formalized by `Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP`, a definition declared in [CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group/index.html#group-otp).

## Group one-time pad ciphertexts are uniform

Let $G$ be a finite group. For every
message $m \in G$, the ciphertext of $m$ under the group one-time pad on $G$, whose key is
drawn uniformly from $G$, is uniformly distributed on $G$.

Formalized by `Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP_ciphertextDist_eq_uniform`, a theorem declared in [CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group/index.html#group-otp-ciphertext-dist-eq-uniform).

## The group one-time pad is perfectly secret

Let $G$ be a finite group. The group
one-time pad on $G$ is perfectly secret: for every probability distribution on messages in $G$
and every ciphertext $c$ that occurs with positive probability, the conditional distribution
of the message given that the ciphertext is $c$ equals the prior distribution of the message.

## Sources

- Katz and Lindell, Lemma 11.15.

Formalized by `Cslib.Crypto.Protocols.PerfectSecrecy.groupOTP_perfectlySecret`, a theorem declared in [CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Crypto/Protocols/PerfectSecrecy/GroupOneTimePad.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group/index.html#group-otp-perfectly-secret).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-time pad over a finite group](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/cryptography/one-time-pad-over-a-finite-group)
