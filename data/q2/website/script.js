const questions = [
    {
        id: "A",
        src: "../../audio_frag_wavs/A octave_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "B",
        src: "../../audio_frag_wavs/B I-V-IV-IV_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "C",
        src: "../../audio_frag_wavs/C I-V-IV-iv_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "D",
        src: "../../audio_frag_wavs/D I-V-iv-iv_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "E",
        src: "../../audio_frag_wavs/E I-v-iv-iv_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "F",
        src: "../../audio_frag_wavs/F i-v-iv-iv_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "G",
        src: "../../audio_frag_wavs/G adj_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "H",
        src: "../../audio_frag_wavs/H I-V-vi-IV_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "I",
        src: "../../audio_frag_wavs/I vi-V-IV-V_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    },
    {
        id: "J",
        src: "../../audio_frag_wavs/J I-vi-IV-V_c_maj_200_bpm.wav",
        listened: false,
        ans: null
    }
];

const questionOrder = ["H", "C", "I", "G", "E", "J", "A", "F", "D", "B"];

let userData = {
    "nationality": localStorage.getItem("nationality"),
    "questions" : localStorage.getItem("questions"),
    "questionIndex": localStorage.getItem("question-index")
}
