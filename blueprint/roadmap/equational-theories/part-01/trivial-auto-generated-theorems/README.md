# Trivial auto-generated theorems

[Approximately 4.5m transitive implications were proven by a transitive reduction of about 15k theorems](https://github.com/teorth/equational_theories/tree/main/equational_theories/Generated/TrivialBruteforce). Most of these implications were derived from being the first automated run to connect the largest equivalence classes, hence creating a large set of transitively closed implications.

Scripts generated theorems to try simple combinations of equation rewrites to reach the desired goal for every unknown implication. The generated proof scripts were run with lean and the successful theorems were extracted. An example of the types of generated rewrites that were tested:

```
repeat intro
apply
```

```
repeat intro
try { rw [<-h] }
try { rw [<-h, <-h] }
try { rw [<-h, <-h, <-h] }
try { rw [<-h, <-h, <-h, <-h] }
try { rw [<-h, <-h, <-h, <-h, <-h] }
repeat rw [h]
```

```
repeat intro
try {
  nth_rewrite 1 [h]
  try { rw [h] }
  try { rw [<-h] }
}
try {
  nth_rewrite 2 [h]
  try { rw [h] }
  try { rw [<-h] }
}
try {
  nth_rewrite 3 [h]
  try { rw [h] }
  try { rw [<-h] }
}
try {
  nth_rewrite 4 [h]
  try { rw [h] }
  try { rw [<-h] }
}
try {
  nth_rewrite 1 [h]
  nth_rewrite 1 [h]
  try { rw [h] }
  try { rw [<-h] }
}
...
```
