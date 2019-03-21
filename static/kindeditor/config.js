KindEditor.ready(function (k) {
    window.editor = k.create('#id_node', {
        resizeType: 1,
        allowPreviewEmoticons: false,
        allowImageRemote: false,
        uploadJson: '/upload/kindeditor',
        width: '800px',
        height: '400px',
    });
});